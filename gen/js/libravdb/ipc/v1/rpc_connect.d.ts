import { AfterTurnKernelRequest, AfterTurnKernelResponse, AssembleContextInternalRequest, AssembleContextInternalResponse, BeforeTurnKernelRequest, BeforeTurnKernelResponse, BootstrapSessionKernelRequest, BootstrapSessionKernelResponse, BumpAccessCountsRequest, BumpAccessCountsResponse, CognitiveMetricsRequest, CognitiveMetricsResponse, CompactSessionRequest, CompactSessionResponse, DaemonStatusRequest, DaemonStatusResponse, DeleteAuthoredDocumentRequest, DeleteAuthoredDocumentResponse, DeleteBatchRequest, DeleteBatchResponse, DeleteRequest, DeleteResponse, DreamPromotionResponse, EnsureCollectionsRequest, EnsureCollectionsResponse, EvictTenantRequest, EvictTenantResponse, ExpandSummaryRequest, ExpandSummaryResponse, ExportMemoryRequest, ExportMemoryResponse, FlushNamespaceRequest, FlushNamespaceResponse, FlushRequest, FlushResponse, GatingScalarRequest, GatingScalarResponse, GetUserCardRequest, GetUserCardResponse, HealthRequest, HealthResponse, IngestMarkdownDocumentRequest, IngestMarkdownDocumentResponse, IngestMessageKernelRequest, IngestMessageKernelResponse, InsertSessionTurnRequest, InsertSessionTurnResponse, InsertTextRequest, InsertTextResponse, ListByMetaRequest, ListByMetaResponse, ListCollectionRequest, ListCollectionResponse, ListLifecycleJournalRequest, ListLifecycleJournalResponse, MarkMemorySupersededRequest, MarkMemorySupersededResponse, MemoryStatusRequest, MemoryStatusResponse, PromoteDreamEntriesRequest, QueryRawSessionRequest, QueryRawSessionResponse, RankCandidatesRequest, RankCandidatesResponse, RebuildIndexRequest, RebuildIndexResponse, ReindexAuthoredDocumentRequest, ReindexAuthoredDocumentResponse, SearchTextCollectionsRequest, SearchTextRequest, SearchTextResponse, SessionLifecycleHintRequest, SessionLifecycleHintResponse, SummarizeMessagesRequest, SummarizeMessagesResponse, UpsertUserCardRequest, UpsertUserCardResponse } from "./rpc_pb.js";
import { MethodKind } from "@bufbuild/protobuf";
/**
 * @generated from service libravdb.ipc.v1.LibravDB
 */
export declare const LibravDB: {
    readonly typeName: "libravdb.ipc.v1.LibravDB";
    readonly methods: {
        /**
         * Session lifecycle
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.Health
         */
        readonly health: {
            readonly name: "Health";
            readonly I: typeof HealthRequest;
            readonly O: typeof HealthResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.Status
         */
        readonly status: {
            readonly name: "Status";
            readonly I: typeof MemoryStatusRequest;
            readonly O: typeof MemoryStatusResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.DaemonStatus
         */
        readonly daemonStatus: {
            readonly name: "DaemonStatus";
            readonly I: typeof DaemonStatusRequest;
            readonly O: typeof DaemonStatusResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.EvictTenant
         */
        readonly evictTenant: {
            readonly name: "EvictTenant";
            readonly I: typeof EvictTenantRequest;
            readonly O: typeof EvictTenantResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.Flush
         */
        readonly flush: {
            readonly name: "Flush";
            readonly I: typeof FlushRequest;
            readonly O: typeof FlushResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.SessionLifecycleHint
         */
        readonly sessionLifecycleHint: {
            readonly name: "SessionLifecycleHint";
            readonly I: typeof SessionLifecycleHintRequest;
            readonly O: typeof SessionLifecycleHintResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.ListLifecycleJournal
         */
        readonly listLifecycleJournal: {
            readonly name: "ListLifecycleJournal";
            readonly I: typeof ListLifecycleJournalRequest;
            readonly O: typeof ListLifecycleJournalResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Collections
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.EnsureCollections
         */
        readonly ensureCollections: {
            readonly name: "EnsureCollections";
            readonly I: typeof EnsureCollectionsRequest;
            readonly O: typeof EnsureCollectionsResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Ingest
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.IngestMarkdownDocument
         */
        readonly ingestMarkdownDocument: {
            readonly name: "IngestMarkdownDocument";
            readonly I: typeof IngestMarkdownDocumentRequest;
            readonly O: typeof IngestMarkdownDocumentResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.PromoteDreamEntries
         */
        readonly promoteDreamEntries: {
            readonly name: "PromoteDreamEntries";
            readonly I: typeof PromoteDreamEntriesRequest;
            readonly O: typeof DreamPromotionResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.ReindexAuthoredDocument
         */
        readonly reindexAuthoredDocument: {
            readonly name: "ReindexAuthoredDocument";
            readonly I: typeof ReindexAuthoredDocumentRequest;
            readonly O: typeof ReindexAuthoredDocumentResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.DeleteAuthoredDocument
         */
        readonly deleteAuthoredDocument: {
            readonly name: "DeleteAuthoredDocument";
            readonly I: typeof DeleteAuthoredDocumentRequest;
            readonly O: typeof DeleteAuthoredDocumentResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.MarkMemorySuperseded
         */
        readonly markMemorySuperseded: {
            readonly name: "MarkMemorySuperseded";
            readonly I: typeof MarkMemorySupersededRequest;
            readonly O: typeof MarkMemorySupersededResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Insert
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.InsertText
         */
        readonly insertText: {
            readonly name: "InsertText";
            readonly I: typeof InsertTextRequest;
            readonly O: typeof InsertTextResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.InsertSessionTurn
         */
        readonly insertSessionTurn: {
            readonly name: "InsertSessionTurn";
            readonly I: typeof InsertSessionTurnRequest;
            readonly O: typeof InsertSessionTurnResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Ranking and gating
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.GatingScalar
         */
        readonly gatingScalar: {
            readonly name: "GatingScalar";
            readonly I: typeof GatingScalarRequest;
            readonly O: typeof GatingScalarResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.SearchText
         */
        readonly searchText: {
            readonly name: "SearchText";
            readonly I: typeof SearchTextRequest;
            readonly O: typeof SearchTextResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.SearchTextCollections
         */
        readonly searchTextCollections: {
            readonly name: "SearchTextCollections";
            readonly I: typeof SearchTextCollectionsRequest;
            readonly O: typeof SearchTextResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.BumpAccessCounts
         */
        readonly bumpAccessCounts: {
            readonly name: "BumpAccessCounts";
            readonly I: typeof BumpAccessCountsRequest;
            readonly O: typeof BumpAccessCountsResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Query
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.ListCollection
         */
        readonly listCollection: {
            readonly name: "ListCollection";
            readonly I: typeof ListCollectionRequest;
            readonly O: typeof ListCollectionResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.ListByMeta
         */
        readonly listByMeta: {
            readonly name: "ListByMeta";
            readonly I: typeof ListByMetaRequest;
            readonly O: typeof ListByMetaResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Memory
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.ExportMemory
         */
        readonly exportMemory: {
            readonly name: "ExportMemory";
            readonly I: typeof ExportMemoryRequest;
            readonly O: typeof ExportMemoryResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.FlushNamespace
         */
        readonly flushNamespace: {
            readonly name: "FlushNamespace";
            readonly I: typeof FlushNamespaceRequest;
            readonly O: typeof FlushNamespaceResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Delete
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.Delete
         */
        readonly delete: {
            readonly name: "Delete";
            readonly I: typeof DeleteRequest;
            readonly O: typeof DeleteResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.DeleteBatch
         */
        readonly deleteBatch: {
            readonly name: "DeleteBatch";
            readonly I: typeof DeleteBatchRequest;
            readonly O: typeof DeleteBatchResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Session
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.CompactSession
         */
        readonly compactSession: {
            readonly name: "CompactSession";
            readonly I: typeof CompactSessionRequest;
            readonly O: typeof CompactSessionResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.SummarizeMessages
         */
        readonly summarizeMessages: {
            readonly name: "SummarizeMessages";
            readonly I: typeof SummarizeMessagesRequest;
            readonly O: typeof SummarizeMessagesResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.ExpandSummary
         */
        readonly expandSummary: {
            readonly name: "ExpandSummary";
            readonly I: typeof ExpandSummaryRequest;
            readonly O: typeof ExpandSummaryResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.QueryRawSession
         */
        readonly queryRawSession: {
            readonly name: "QueryRawSession";
            readonly I: typeof QueryRawSessionRequest;
            readonly O: typeof QueryRawSessionResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Index
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.RebuildIndex
         */
        readonly rebuildIndex: {
            readonly name: "RebuildIndex";
            readonly I: typeof RebuildIndexRequest;
            readonly O: typeof RebuildIndexResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Kernel
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.BootstrapSessionKernel
         */
        readonly bootstrapSessionKernel: {
            readonly name: "BootstrapSessionKernel";
            readonly I: typeof BootstrapSessionKernelRequest;
            readonly O: typeof BootstrapSessionKernelResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.IngestMessageKernel
         */
        readonly ingestMessageKernel: {
            readonly name: "IngestMessageKernel";
            readonly I: typeof IngestMessageKernelRequest;
            readonly O: typeof IngestMessageKernelResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.BeforeTurnKernel
         */
        readonly beforeTurnKernel: {
            readonly name: "BeforeTurnKernel";
            readonly I: typeof BeforeTurnKernelRequest;
            readonly O: typeof BeforeTurnKernelResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.AfterTurnKernel
         */
        readonly afterTurnKernel: {
            readonly name: "AfterTurnKernel";
            readonly I: typeof AfterTurnKernelRequest;
            readonly O: typeof AfterTurnKernelResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * User Card
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.UpsertUserCard
         */
        readonly upsertUserCard: {
            readonly name: "UpsertUserCard";
            readonly I: typeof UpsertUserCardRequest;
            readonly O: typeof UpsertUserCardResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.GetUserCard
         */
        readonly getUserCard: {
            readonly name: "GetUserCard";
            readonly I: typeof GetUserCardRequest;
            readonly O: typeof GetUserCardResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * @generated from rpc libravdb.ipc.v1.LibravDB.AssembleContextInternal
         */
        readonly assembleContextInternal: {
            readonly name: "AssembleContextInternal";
            readonly I: typeof AssembleContextInternalRequest;
            readonly O: typeof AssembleContextInternalResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Ranking
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.RankCandidates
         */
        readonly rankCandidates: {
            readonly name: "RankCandidates";
            readonly I: typeof RankCandidatesRequest;
            readonly O: typeof RankCandidatesResponse;
            readonly kind: MethodKind.Unary;
        };
        /**
         * Cognitive
         *
         * @generated from rpc libravdb.ipc.v1.LibravDB.CognitiveMetrics
         */
        readonly cognitiveMetrics: {
            readonly name: "CognitiveMetrics";
            readonly I: typeof CognitiveMetricsRequest;
            readonly O: typeof CognitiveMetricsResponse;
            readonly kind: MethodKind.Unary;
        };
    };
};
//# sourceMappingURL=rpc_connect.d.ts.map