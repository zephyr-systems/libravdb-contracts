package main

import (
	"fmt"
	"os"

	ipcv1 "github.com/xDarkicex/libravdb-contracts/libravdb/ipc/v1"
	"google.golang.org/protobuf/proto"
)

func fail(format string, args ...any) {
	fmt.Fprintf(os.Stderr, "FAIL: "+format+"\n", args...)
	os.Exit(1)
}

func main() {
	empty := &ipcv1.AssembleConfigOverrides{}
	fmt.Printf("empty: top_k_present=%v get_top_k=%d\n", empty.TopK != nil, empty.GetTopK())

	zero := &ipcv1.AssembleConfigOverrides{TopK: proto.Int32(0)}
	fmt.Printf("set_zero_before_marshal: top_k_present=%v get_top_k=%d\n", zero.TopK != nil, zero.GetTopK())

	bEmpty, err := proto.Marshal(empty)
	if err != nil {
		fail("marshal empty: %v", err)
	}
	bZero, err := proto.Marshal(zero)
	if err != nil {
		fail("marshal zero: %v", err)
	}
	fmt.Printf("wire_sizes: empty=%d zero=%d\n", len(bEmpty), len(bZero))

	var emptyRT ipcv1.AssembleConfigOverrides
	if err := proto.Unmarshal(bEmpty, &emptyRT); err != nil {
		fail("unmarshal empty: %v", err)
	}
	var zeroRT ipcv1.AssembleConfigOverrides
	if err := proto.Unmarshal(bZero, &zeroRT); err != nil {
		fail("unmarshal zero: %v", err)
	}

	fmt.Printf("empty_after_roundtrip: top_k_present=%v get_top_k=%d\n", emptyRT.TopK != nil, emptyRT.GetTopK())
	fmt.Printf("zero_after_roundtrip: top_k_present=%v get_top_k=%d\n", zeroRT.TopK != nil, zeroRT.GetTopK())

	if emptyRT.TopK != nil {
		fail("expected empty.TopK to remain nil after roundtrip")
	}
	if zeroRT.TopK == nil {
		fail("expected zero.TopK to remain present after roundtrip")
	}
	if zeroRT.GetTopK() != 0 {
		fail("expected zero.TopK value to remain 0 after roundtrip; got %d", zeroRT.GetTopK())
	}

	fmt.Println("PASS: unset-vs-zero presence for top_k is preserved")
}
