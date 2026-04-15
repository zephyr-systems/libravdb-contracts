# libravdb-contracts

This repository is the source of truth for the LibraVDB IPC protocol.

## Tooling

We use [Buf](https://buf.build/) for deterministic code generation.

### Pinned Versions

To ensure bit-perfect parity across environments, use these versions:

- **Buf CLI**: `v2`
- **Go Plugin**: `buf.build/protocolbuffers/go:v1.32.0`
- **TypeScript Plugin**: `buf.build/bufbuild/es:v1.7.2` (Protobuf-ES)
- **TypeScript Generator Package**: `@bufbuild/protoc-gen-es` `v2.10.0`
- **TypeScript Runtime Package**: `@bufbuild/protobuf` `v2.10.0`

### Generation

Run the following command from the root of this repository:

```bash
buf generate
```

This will produce:
- `libravdb/ipc/v1/rpc.pb.go`: canonical Go types for the daemon.
- `gen/ts/`: TypeScript types and runtime for the plugin.

### Linting

Run schema linting from the repository root:

```bash
buf lint
```

---

## Generator Choice: Protobuf-ES

We have chosen `protobuf-es` over `ts-proto` for the following reasons:

1. **Modern Standard**: It is the official recommended path for TypeScript by the creators of Buf.
2. **Type Safety**: It provides better integration with modern TypeScript features and avoids the "any" pollution often found in older generators.
3. **Determinism**: By using Buf's remote plugins, we guarantee that every developer generates identical code regardless of their local `protoc` installation.
4. **Performance**: It produces smaller, more efficient code that leverage's JavaScript's native binary handling.
