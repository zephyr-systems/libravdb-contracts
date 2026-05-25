from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IngestMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INGEST_MODE_REPLACE: _ClassVar[IngestMode]
    INGEST_MODE_APPEND: _ClassVar[IngestMode]
INGEST_MODE_REPLACE: IngestMode
INGEST_MODE_APPEND: IngestMode

class RpcRequest(_message.Message):
    __slots__ = ("id", "method", "params")
    ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    id: int
    method: str
    params: bytes
    def __init__(self, id: _Optional[int] = ..., method: _Optional[str] = ..., params: _Optional[bytes] = ...) -> None: ...

class RpcResponse(_message.Message):
    __slots__ = ("id", "result", "error")
    ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    id: int
    result: bytes
    error: RpcError
    def __init__(self, id: _Optional[int] = ..., result: _Optional[bytes] = ..., error: _Optional[_Union[RpcError, _Mapping]] = ...) -> None: ...

class RpcError(_message.Message):
    __slots__ = ("message", "code")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    message: str
    code: int
    def __init__(self, message: _Optional[str] = ..., code: _Optional[int] = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchResult(_message.Message):
    __slots__ = ("id", "score", "text", "metadata_json", "version")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    score: float
    text: str
    metadata_json: bytes
    version: int
    def __init__(self, id: _Optional[str] = ..., score: _Optional[float] = ..., text: _Optional[str] = ..., metadata_json: _Optional[bytes] = ..., version: _Optional[int] = ...) -> None: ...

class MarkdownSourceMeta(_message.Message):
    __slots__ = ("source_root", "source_path", "source_kind", "file_hash", "source_size", "source_mtime_ms", "ingest_version", "hash_backend", "source_ctime_ms")
    SOURCE_ROOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MTIME_MS_FIELD_NUMBER: _ClassVar[int]
    INGEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    HASH_BACKEND_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CTIME_MS_FIELD_NUMBER: _ClassVar[int]
    source_root: str
    source_path: str
    source_kind: str
    file_hash: str
    source_size: int
    source_mtime_ms: int
    ingest_version: int
    hash_backend: str
    source_ctime_ms: int
    def __init__(self, source_root: _Optional[str] = ..., source_path: _Optional[str] = ..., source_kind: _Optional[str] = ..., file_hash: _Optional[str] = ..., source_size: _Optional[int] = ..., source_mtime_ms: _Optional[int] = ..., ingest_version: _Optional[int] = ..., hash_backend: _Optional[str] = ..., source_ctime_ms: _Optional[int] = ...) -> None: ...

class DreamPromotionEntry(_message.Message):
    __slots__ = ("text", "score", "recall_count", "unique_queries", "section", "line", "source_line", "metadata_json")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RECALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    SECTION_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LINE_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    text: str
    score: float
    recall_count: int
    unique_queries: int
    section: str
    line: int
    source_line: int
    metadata_json: bytes
    def __init__(self, text: _Optional[str] = ..., score: _Optional[float] = ..., recall_count: _Optional[int] = ..., unique_queries: _Optional[int] = ..., section: _Optional[str] = ..., line: _Optional[int] = ..., source_line: _Optional[int] = ..., metadata_json: _Optional[bytes] = ...) -> None: ...

class IngestFeedback(_message.Message):
    __slots__ = ("queue_depth", "queue_capacity", "accept_more", "retry_after_ms", "processing_time_us", "nodes_accepted", "nodes_rejected", "tokens_ingested", "token_burst_limit", "wal_depth", "wal_capacity")
    QUEUE_DEPTH_FIELD_NUMBER: _ClassVar[int]
    QUEUE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_MORE_FIELD_NUMBER: _ClassVar[int]
    RETRY_AFTER_MS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_US_FIELD_NUMBER: _ClassVar[int]
    NODES_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    NODES_REJECTED_FIELD_NUMBER: _ClassVar[int]
    TOKENS_INGESTED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_BURST_LIMIT_FIELD_NUMBER: _ClassVar[int]
    WAL_DEPTH_FIELD_NUMBER: _ClassVar[int]
    WAL_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    queue_depth: int
    queue_capacity: int
    accept_more: bool
    retry_after_ms: int
    processing_time_us: int
    nodes_accepted: int
    nodes_rejected: int
    tokens_ingested: int
    token_burst_limit: int
    wal_depth: int
    wal_capacity: int
    def __init__(self, queue_depth: _Optional[int] = ..., queue_capacity: _Optional[int] = ..., accept_more: bool = ..., retry_after_ms: _Optional[int] = ..., processing_time_us: _Optional[int] = ..., nodes_accepted: _Optional[int] = ..., nodes_rejected: _Optional[int] = ..., tokens_ingested: _Optional[int] = ..., token_burst_limit: _Optional[int] = ..., wal_depth: _Optional[int] = ..., wal_capacity: _Optional[int] = ...) -> None: ...

class AccessCountUpdate(_message.Message):
    __slots__ = ("collection", "ids")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    collection: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class KernelMessage(_message.Message):
    __slots__ = ("role", "content", "id")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    role: str
    content: str
    id: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class AssembleContextInternalResponse(_message.Message):
    __slots__ = ("messages", "estimated_tokens", "system_prompt_addition", "debug")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOKENS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_PROMPT_ADDITION_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[KernelMessage]
    estimated_tokens: int
    system_prompt_addition: str
    debug: AssemblyDebug
    def __init__(self, messages: _Optional[_Iterable[_Union[KernelMessage, _Mapping]]] = ..., estimated_tokens: _Optional[int] = ..., system_prompt_addition: _Optional[str] = ..., debug: _Optional[_Union[AssemblyDebug, _Mapping]] = ...) -> None: ...

class PredictedContext(_message.Message):
    __slots__ = ("id", "text", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    text: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., text: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class AssemblyDebug(_message.Message):
    __slots__ = ("recovery_trigger_fired", "cross_session_raw_recovery", "recovery_reserve_tokens", "recovery_deduped_order", "recovery_fitted_order")
    RECOVERY_TRIGGER_FIRED_FIELD_NUMBER: _ClassVar[int]
    CROSS_SESSION_RAW_RECOVERY_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_RESERVE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_DEDUPED_ORDER_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FITTED_ORDER_FIELD_NUMBER: _ClassVar[int]
    recovery_trigger_fired: bool
    cross_session_raw_recovery: bool
    recovery_reserve_tokens: int
    recovery_deduped_order: _containers.RepeatedCompositeFieldContainer[RecoveryOrderEntry]
    recovery_fitted_order: _containers.RepeatedCompositeFieldContainer[RecoveryOrderEntry]
    def __init__(self, recovery_trigger_fired: bool = ..., cross_session_raw_recovery: bool = ..., recovery_reserve_tokens: _Optional[int] = ..., recovery_deduped_order: _Optional[_Iterable[_Union[RecoveryOrderEntry, _Mapping]]] = ..., recovery_fitted_order: _Optional[_Iterable[_Union[RecoveryOrderEntry, _Mapping]]] = ...) -> None: ...

class RecoveryOrderEntry(_message.Message):
    __slots__ = ("id", "recovery_scope", "final_score", "token_estimate")
    ID_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_SCOPE_FIELD_NUMBER: _ClassVar[int]
    FINAL_SCORE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ESTIMATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    recovery_scope: str
    final_score: float
    token_estimate: int
    def __init__(self, id: _Optional[str] = ..., recovery_scope: _Optional[str] = ..., final_score: _Optional[float] = ..., token_estimate: _Optional[int] = ...) -> None: ...

class AssembleConfigOverrides(_message.Message):
    __slots__ = ("use_session_recall_projection", "use_session_summary_search_experiment", "token_budget_fraction", "authored_hard_budget_fraction", "authored_soft_budget_fraction", "elevated_guidance_budget_fraction", "top_k", "continuity_min_turns", "continuity_tail_budget_tokens", "continuity_prior_context_tokens", "compact_threshold", "compact_session_token_budget", "section7_theta1", "section7_kappa", "section7_hop_eta", "section7_hop_threshold", "section7_coarse_top_k", "section7_second_pass_top_k", "section7_authority_recency_lambda", "section7_authority_recency_weight", "section7_authority_frequency_weight", "section7_authority_authored_weight", "recovery_floor_score", "recovery_min_top_k", "recovery_min_confidence_mean", "recency_lambda_session", "recency_lambda_user", "recency_lambda_global", "ingestion_gate_threshold", "section7_authority_salience_weight", "section7_recency_access_lambda")
    USE_SESSION_RECALL_PROJECTION_FIELD_NUMBER: _ClassVar[int]
    USE_SESSION_SUMMARY_SEARCH_EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_BUDGET_FRACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORED_HARD_BUDGET_FRACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORED_SOFT_BUDGET_FRACTION_FIELD_NUMBER: _ClassVar[int]
    ELEVATED_GUIDANCE_BUDGET_FRACTION_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_MIN_TURNS_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_TAIL_BUDGET_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_PRIOR_CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    COMPACT_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    COMPACT_SESSION_TOKEN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    SECTION7_THETA1_FIELD_NUMBER: _ClassVar[int]
    SECTION7_KAPPA_FIELD_NUMBER: _ClassVar[int]
    SECTION7_HOP_ETA_FIELD_NUMBER: _ClassVar[int]
    SECTION7_HOP_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SECTION7_COARSE_TOP_K_FIELD_NUMBER: _ClassVar[int]
    SECTION7_SECOND_PASS_TOP_K_FIELD_NUMBER: _ClassVar[int]
    SECTION7_AUTHORITY_RECENCY_LAMBDA_FIELD_NUMBER: _ClassVar[int]
    SECTION7_AUTHORITY_RECENCY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SECTION7_AUTHORITY_FREQUENCY_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SECTION7_AUTHORITY_AUTHORED_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_FLOOR_SCORE_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MIN_TOP_K_FIELD_NUMBER: _ClassVar[int]
    RECOVERY_MIN_CONFIDENCE_MEAN_FIELD_NUMBER: _ClassVar[int]
    RECENCY_LAMBDA_SESSION_FIELD_NUMBER: _ClassVar[int]
    RECENCY_LAMBDA_USER_FIELD_NUMBER: _ClassVar[int]
    RECENCY_LAMBDA_GLOBAL_FIELD_NUMBER: _ClassVar[int]
    INGESTION_GATE_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    SECTION7_AUTHORITY_SALIENCE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    SECTION7_RECENCY_ACCESS_LAMBDA_FIELD_NUMBER: _ClassVar[int]
    use_session_recall_projection: bool
    use_session_summary_search_experiment: bool
    token_budget_fraction: float
    authored_hard_budget_fraction: float
    authored_soft_budget_fraction: float
    elevated_guidance_budget_fraction: float
    top_k: int
    continuity_min_turns: int
    continuity_tail_budget_tokens: int
    continuity_prior_context_tokens: int
    compact_threshold: int
    compact_session_token_budget: int
    section7_theta1: float
    section7_kappa: float
    section7_hop_eta: float
    section7_hop_threshold: float
    section7_coarse_top_k: int
    section7_second_pass_top_k: int
    section7_authority_recency_lambda: float
    section7_authority_recency_weight: float
    section7_authority_frequency_weight: float
    section7_authority_authored_weight: float
    recovery_floor_score: float
    recovery_min_top_k: int
    recovery_min_confidence_mean: float
    recency_lambda_session: float
    recency_lambda_user: float
    recency_lambda_global: float
    ingestion_gate_threshold: float
    section7_authority_salience_weight: float
    section7_recency_access_lambda: float
    def __init__(self, use_session_recall_projection: bool = ..., use_session_summary_search_experiment: bool = ..., token_budget_fraction: _Optional[float] = ..., authored_hard_budget_fraction: _Optional[float] = ..., authored_soft_budget_fraction: _Optional[float] = ..., elevated_guidance_budget_fraction: _Optional[float] = ..., top_k: _Optional[int] = ..., continuity_min_turns: _Optional[int] = ..., continuity_tail_budget_tokens: _Optional[int] = ..., continuity_prior_context_tokens: _Optional[int] = ..., compact_threshold: _Optional[int] = ..., compact_session_token_budget: _Optional[int] = ..., section7_theta1: _Optional[float] = ..., section7_kappa: _Optional[float] = ..., section7_hop_eta: _Optional[float] = ..., section7_hop_threshold: _Optional[float] = ..., section7_coarse_top_k: _Optional[int] = ..., section7_second_pass_top_k: _Optional[int] = ..., section7_authority_recency_lambda: _Optional[float] = ..., section7_authority_recency_weight: _Optional[float] = ..., section7_authority_frequency_weight: _Optional[float] = ..., section7_authority_authored_weight: _Optional[float] = ..., recovery_floor_score: _Optional[float] = ..., recovery_min_top_k: _Optional[int] = ..., recovery_min_confidence_mean: _Optional[float] = ..., recency_lambda_session: _Optional[float] = ..., recency_lambda_user: _Optional[float] = ..., recency_lambda_global: _Optional[float] = ..., ingestion_gate_threshold: _Optional[float] = ..., section7_authority_salience_weight: _Optional[float] = ..., section7_recency_access_lambda: _Optional[float] = ...) -> None: ...

class RankCandidate(_message.Message):
    __slots__ = ("id", "text", "score", "metadata_json")
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    id: str
    text: str
    score: float
    metadata_json: bytes
    def __init__(self, id: _Optional[str] = ..., text: _Optional[str] = ..., score: _Optional[float] = ..., metadata_json: _Optional[bytes] = ...) -> None: ...

class HealthResponse(_message.Message):
    __slots__ = ("ok", "message")
    OK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    message: str
    def __init__(self, ok: bool = ..., message: _Optional[str] = ...) -> None: ...

class CompactSessionResponse(_message.Message):
    __slots__ = ("did_compact", "clusters_formed", "clusters_declined", "turns_removed", "summary_method", "mean_confidence", "summary_text")
    DID_COMPACT_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FORMED_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_DECLINED_FIELD_NUMBER: _ClassVar[int]
    TURNS_REMOVED_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_METHOD_FIELD_NUMBER: _ClassVar[int]
    MEAN_CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_TEXT_FIELD_NUMBER: _ClassVar[int]
    did_compact: bool
    clusters_formed: int
    clusters_declined: int
    turns_removed: int
    summary_method: str
    mean_confidence: float
    summary_text: str
    def __init__(self, did_compact: bool = ..., clusters_formed: _Optional[int] = ..., clusters_declined: _Optional[int] = ..., turns_removed: _Optional[int] = ..., summary_method: _Optional[str] = ..., mean_confidence: _Optional[float] = ..., summary_text: _Optional[str] = ...) -> None: ...

class GatingScalarResponse(_message.Message):
    __slots__ = ("g", "t", "h", "r", "d", "input_freq", "mem_saturation", "p", "a", "dtech", "gconv", "gtech")
    G_FIELD_NUMBER: _ClassVar[int]
    T_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    INPUT_FREQ_FIELD_NUMBER: _ClassVar[int]
    MEM_SATURATION_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    DTECH_FIELD_NUMBER: _ClassVar[int]
    GCONV_FIELD_NUMBER: _ClassVar[int]
    GTECH_FIELD_NUMBER: _ClassVar[int]
    g: float
    t: float
    h: float
    r: float
    d: float
    input_freq: float
    mem_saturation: float
    p: float
    a: float
    dtech: float
    gconv: float
    gtech: float
    def __init__(self, g: _Optional[float] = ..., t: _Optional[float] = ..., h: _Optional[float] = ..., r: _Optional[float] = ..., d: _Optional[float] = ..., input_freq: _Optional[float] = ..., mem_saturation: _Optional[float] = ..., p: _Optional[float] = ..., a: _Optional[float] = ..., dtech: _Optional[float] = ..., gconv: _Optional[float] = ..., gtech: _Optional[float] = ...) -> None: ...

class ExportMemoryRecord(_message.Message):
    __slots__ = ("collection", "id", "text", "metadata_json")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    collection: str
    id: str
    text: str
    metadata_json: bytes
    def __init__(self, collection: _Optional[str] = ..., id: _Optional[str] = ..., text: _Optional[str] = ..., metadata_json: _Optional[bytes] = ...) -> None: ...

class EnsureCollectionsRequest(_message.Message):
    __slots__ = ("collections",)
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collections: _Optional[_Iterable[str]] = ...) -> None: ...

class EnsureCollectionsResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class InsertTextRequest(_message.Message):
    __slots__ = ("collection", "id", "text", "metadata_json")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    collection: str
    id: str
    text: str
    metadata_json: bytes
    def __init__(self, collection: _Optional[str] = ..., id: _Optional[str] = ..., text: _Optional[str] = ..., metadata_json: _Optional[bytes] = ...) -> None: ...

class InsertTextResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class InsertSessionTurnRequest(_message.Message):
    __slots__ = ("session_id", "id", "text", "metadata_json")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    METADATA_JSON_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    id: str
    text: str
    metadata_json: bytes
    def __init__(self, session_id: _Optional[str] = ..., id: _Optional[str] = ..., text: _Optional[str] = ..., metadata_json: _Optional[bytes] = ...) -> None: ...

class InsertSessionTurnResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class IngestMarkdownDocumentRequest(_message.Message):
    __slots__ = ("source_doc", "text", "tokenizer_id", "core_doc", "source_meta", "mode")
    SOURCE_DOC_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKENIZER_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_DOC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_META_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    source_doc: str
    text: str
    tokenizer_id: str
    core_doc: bool
    source_meta: MarkdownSourceMeta
    mode: IngestMode
    def __init__(self, source_doc: _Optional[str] = ..., text: _Optional[str] = ..., tokenizer_id: _Optional[str] = ..., core_doc: bool = ..., source_meta: _Optional[_Union[MarkdownSourceMeta, _Mapping]] = ..., mode: _Optional[_Union[IngestMode, str]] = ...) -> None: ...

class IngestMarkdownDocumentResponse(_message.Message):
    __slots__ = ("ok", "feedback")
    OK_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    feedback: IngestFeedback
    def __init__(self, ok: bool = ..., feedback: _Optional[_Union[IngestFeedback, _Mapping]] = ...) -> None: ...

class DeleteAuthoredDocumentRequest(_message.Message):
    __slots__ = ("source_doc",)
    SOURCE_DOC_FIELD_NUMBER: _ClassVar[int]
    source_doc: str
    def __init__(self, source_doc: _Optional[str] = ...) -> None: ...

class DeleteAuthoredDocumentResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class PromoteDreamEntriesRequest(_message.Message):
    __slots__ = ("user_id", "source_doc", "source_root", "source_path", "source_kind", "file_hash", "source_size", "source_mtime_ms", "ingest_version", "hash_backend", "entries", "source_ctime_ms")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_DOC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ROOT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_KIND_FIELD_NUMBER: _ClassVar[int]
    FILE_HASH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_SIZE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_MTIME_MS_FIELD_NUMBER: _ClassVar[int]
    INGEST_VERSION_FIELD_NUMBER: _ClassVar[int]
    HASH_BACKEND_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CTIME_MS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    source_doc: str
    source_root: str
    source_path: str
    source_kind: str
    file_hash: str
    source_size: int
    source_mtime_ms: int
    ingest_version: int
    hash_backend: str
    entries: _containers.RepeatedCompositeFieldContainer[DreamPromotionEntry]
    source_ctime_ms: int
    def __init__(self, user_id: _Optional[str] = ..., source_doc: _Optional[str] = ..., source_root: _Optional[str] = ..., source_path: _Optional[str] = ..., source_kind: _Optional[str] = ..., file_hash: _Optional[str] = ..., source_size: _Optional[int] = ..., source_mtime_ms: _Optional[int] = ..., ingest_version: _Optional[int] = ..., hash_backend: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[DreamPromotionEntry, _Mapping]]] = ..., source_ctime_ms: _Optional[int] = ...) -> None: ...

class DreamPromotionResponse(_message.Message):
    __slots__ = ("promoted", "rejected", "feedback")
    PROMOTED_FIELD_NUMBER: _ClassVar[int]
    REJECTED_FIELD_NUMBER: _ClassVar[int]
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    promoted: int
    rejected: int
    feedback: IngestFeedback
    def __init__(self, promoted: _Optional[int] = ..., rejected: _Optional[int] = ..., feedback: _Optional[_Union[IngestFeedback, _Mapping]] = ...) -> None: ...

class SearchTextRequest(_message.Message):
    __slots__ = ("collection", "text", "k", "exclude_ids")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_IDS_FIELD_NUMBER: _ClassVar[int]
    collection: str
    text: str
    k: int
    exclude_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection: _Optional[str] = ..., text: _Optional[str] = ..., k: _Optional[int] = ..., exclude_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class SearchTextCollectionsRequest(_message.Message):
    __slots__ = ("collections", "text", "k", "exclude_by_collection")
    class ExcludeByCollectionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_BY_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collections: _containers.RepeatedScalarFieldContainer[str]
    text: str
    k: int
    exclude_by_collection: _containers.MessageMap[str, StringList]
    def __init__(self, collections: _Optional[_Iterable[str]] = ..., text: _Optional[str] = ..., k: _Optional[int] = ..., exclude_by_collection: _Optional[_Mapping[str, StringList]] = ...) -> None: ...

class SearchTextResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ...) -> None: ...

class ListByMetaRequest(_message.Message):
    __slots__ = ("collection", "key", "value")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    collection: str
    key: str
    value: str
    def __init__(self, collection: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class ListCollectionRequest(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: str
    def __init__(self, collection: _Optional[str] = ...) -> None: ...

class ExpandSummaryRequest(_message.Message):
    __slots__ = ("session_id", "summary_id", "max_depth")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    summary_id: str
    max_depth: int
    def __init__(self, session_id: _Optional[str] = ..., summary_id: _Optional[str] = ..., max_depth: _Optional[int] = ...) -> None: ...

class QueryRawSessionRequest(_message.Message):
    __slots__ = ("session_id", "text", "k", "exclude_ids")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    K_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_IDS_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    text: str
    k: int
    exclude_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_id: _Optional[str] = ..., text: _Optional[str] = ..., k: _Optional[int] = ..., exclude_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListLifecycleJournalRequest(_message.Message):
    __slots__ = ("session_id", "limit")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    limit: int
    def __init__(self, session_id: _Optional[str] = ..., limit: _Optional[int] = ...) -> None: ...

class BumpAccessCountsRequest(_message.Message):
    __slots__ = ("updates",)
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[AccessCountUpdate]
    def __init__(self, updates: _Optional[_Iterable[_Union[AccessCountUpdate, _Mapping]]] = ...) -> None: ...

class BumpAccessCountsResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("collection", "id")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    collection: str
    id: str
    def __init__(self, collection: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class DeleteBatchRequest(_message.Message):
    __slots__ = ("collection", "ids")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    collection: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collection: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...

class DeleteBatchResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class CompactSessionRequest(_message.Message):
    __slots__ = ("session_id", "force", "target_size", "continuity_min_turns", "continuity_tail_budget_tokens", "continuity_prior_context_tokens", "current_token_count", "context_window_size")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_SIZE_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_MIN_TURNS_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_TAIL_BUDGET_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CONTINUITY_PRIOR_CONTEXT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_WINDOW_SIZE_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    force: bool
    target_size: int
    continuity_min_turns: int
    continuity_tail_budget_tokens: int
    continuity_prior_context_tokens: int
    current_token_count: int
    context_window_size: int
    def __init__(self, session_id: _Optional[str] = ..., force: bool = ..., target_size: _Optional[int] = ..., continuity_min_turns: _Optional[int] = ..., continuity_tail_budget_tokens: _Optional[int] = ..., continuity_prior_context_tokens: _Optional[int] = ..., current_token_count: _Optional[int] = ..., context_window_size: _Optional[int] = ...) -> None: ...

class GatingScalarRequest(_message.Message):
    __slots__ = ("user_id", "text")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    text: str
    def __init__(self, user_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class FlushNamespaceRequest(_message.Message):
    __slots__ = ("user_id", "namespace")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class SessionLifecycleHintRequest(_message.Message):
    __slots__ = ("hook", "reason", "session_file", "session_id", "session_key", "agent_id", "workspace_dir", "message_count", "duration_ms", "transcript_archived", "next_session_id", "next_session_key")
    HOOK_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    SESSION_FILE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_DIR_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TRANSCRIPT_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    NEXT_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    hook: str
    reason: str
    session_file: str
    session_id: str
    session_key: str
    agent_id: str
    workspace_dir: str
    message_count: int
    duration_ms: int
    transcript_archived: bool
    next_session_id: str
    next_session_key: str
    def __init__(self, hook: _Optional[str] = ..., reason: _Optional[str] = ..., session_file: _Optional[str] = ..., session_id: _Optional[str] = ..., session_key: _Optional[str] = ..., agent_id: _Optional[str] = ..., workspace_dir: _Optional[str] = ..., message_count: _Optional[int] = ..., duration_ms: _Optional[int] = ..., transcript_archived: bool = ..., next_session_id: _Optional[str] = ..., next_session_key: _Optional[str] = ...) -> None: ...

class SessionLifecycleHintResponse(_message.Message):
    __slots__ = ("ok", "hook", "session_id", "reason")
    OK_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    hook: str
    session_id: str
    reason: str
    def __init__(self, ok: bool = ..., hook: _Optional[str] = ..., session_id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class MemoryStatusResponse(_message.Message):
    __slots__ = ("ok", "message", "turn_count", "memory_count", "lifecycle_hint_count", "gating_threshold", "abstractive_ready", "embedding_profile")
    OK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TURN_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LIFECYCLE_HINT_COUNT_FIELD_NUMBER: _ClassVar[int]
    GATING_THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    ABSTRACTIVE_READY_FIELD_NUMBER: _ClassVar[int]
    EMBEDDING_PROFILE_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    message: str
    turn_count: int
    memory_count: int
    lifecycle_hint_count: int
    gating_threshold: float
    abstractive_ready: bool
    embedding_profile: str
    def __init__(self, ok: bool = ..., message: _Optional[str] = ..., turn_count: _Optional[int] = ..., memory_count: _Optional[int] = ..., lifecycle_hint_count: _Optional[int] = ..., gating_threshold: _Optional[float] = ..., abstractive_ready: bool = ..., embedding_profile: _Optional[str] = ...) -> None: ...

class ExportMemoryRequest(_message.Message):
    __slots__ = ("user_id", "namespace")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    namespace: str
    def __init__(self, user_id: _Optional[str] = ..., namespace: _Optional[str] = ...) -> None: ...

class ExportMemoryResponse(_message.Message):
    __slots__ = ("records",)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[ExportMemoryRecord]
    def __init__(self, records: _Optional[_Iterable[_Union[ExportMemoryRecord, _Mapping]]] = ...) -> None: ...

class FlushNamespaceResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class FlushResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class BootstrapSessionKernelRequest(_message.Message):
    __slots__ = ("session_id", "session_key", "user_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_key: str
    user_id: str
    def __init__(self, session_id: _Optional[str] = ..., session_key: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class BootstrapSessionKernelResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class IngestMessageKernelRequest(_message.Message):
    __slots__ = ("session_id", "session_key", "user_id", "message", "is_heartbeat")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_key: str
    user_id: str
    message: KernelMessage
    is_heartbeat: bool
    def __init__(self, session_id: _Optional[str] = ..., session_key: _Optional[str] = ..., user_id: _Optional[str] = ..., message: _Optional[_Union[KernelMessage, _Mapping]] = ..., is_heartbeat: bool = ...) -> None: ...

class IngestMessageKernelResponse(_message.Message):
    __slots__ = ("ok", "ingested")
    OK_FIELD_NUMBER: _ClassVar[int]
    INGESTED_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    ingested: int
    def __init__(self, ok: bool = ..., ingested: _Optional[int] = ...) -> None: ...

class AfterTurnKernelRequest(_message.Message):
    __slots__ = ("session_id", "session_key", "user_id", "messages", "pre_prompt_message_count", "is_heartbeat")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PRE_PROMPT_MESSAGE_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_key: str
    user_id: str
    messages: _containers.RepeatedCompositeFieldContainer[KernelMessage]
    pre_prompt_message_count: int
    is_heartbeat: bool
    def __init__(self, session_id: _Optional[str] = ..., session_key: _Optional[str] = ..., user_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[KernelMessage, _Mapping]]] = ..., pre_prompt_message_count: _Optional[int] = ..., is_heartbeat: bool = ...) -> None: ...

class AfterTurnKernelResponse(_message.Message):
    __slots__ = ("ok", "predictions")
    OK_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    predictions: _containers.RepeatedCompositeFieldContainer[PredictedContext]
    def __init__(self, ok: bool = ..., predictions: _Optional[_Iterable[_Union[PredictedContext, _Mapping]]] = ...) -> None: ...

class AssembleContextInternalRequest(_message.Message):
    __slots__ = ("session_id", "session_key", "user_id", "messages", "token_budget", "prompt", "emit_debug", "config")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_KEY_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOKEN_BUDGET_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    EMIT_DEBUG_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    session_key: str
    user_id: str
    messages: _containers.RepeatedCompositeFieldContainer[KernelMessage]
    token_budget: int
    prompt: str
    emit_debug: bool
    config: AssembleConfigOverrides
    def __init__(self, session_id: _Optional[str] = ..., session_key: _Optional[str] = ..., user_id: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[KernelMessage, _Mapping]]] = ..., token_budget: _Optional[int] = ..., prompt: _Optional[str] = ..., emit_debug: bool = ..., config: _Optional[_Union[AssembleConfigOverrides, _Mapping]] = ...) -> None: ...

class RankCandidatesRequest(_message.Message):
    __slots__ = ("candidates", "query_text", "session_id", "user_id", "k1", "k2")
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    K1_FIELD_NUMBER: _ClassVar[int]
    K2_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[RankCandidate]
    query_text: str
    session_id: str
    user_id: str
    k1: int
    k2: int
    def __init__(self, candidates: _Optional[_Iterable[_Union[RankCandidate, _Mapping]]] = ..., query_text: _Optional[str] = ..., session_id: _Optional[str] = ..., user_id: _Optional[str] = ..., k1: _Optional[int] = ..., k2: _Optional[int] = ...) -> None: ...

class RankCandidatesResponse(_message.Message):
    __slots__ = ("ranked",)
    RANKED_FIELD_NUMBER: _ClassVar[int]
    ranked: _containers.RepeatedCompositeFieldContainer[RankCandidate]
    def __init__(self, ranked: _Optional[_Iterable[_Union[RankCandidate, _Mapping]]] = ...) -> None: ...

class RebuildIndexRequest(_message.Message):
    __slots__ = ("namespace", "collections")
    NAMESPACE_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    namespace: str
    collections: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace: _Optional[str] = ..., collections: _Optional[_Iterable[str]] = ...) -> None: ...

class RebuildIndexResponse(_message.Message):
    __slots__ = ("collections_processed", "records_reindexed", "collections_recreated", "errors")
    COLLECTIONS_PROCESSED_FIELD_NUMBER: _ClassVar[int]
    RECORDS_REINDEXED_FIELD_NUMBER: _ClassVar[int]
    COLLECTIONS_RECREATED_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    collections_processed: int
    records_reindexed: int
    collections_recreated: int
    errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, collections_processed: _Optional[int] = ..., records_reindexed: _Optional[int] = ..., collections_recreated: _Optional[int] = ..., errors: _Optional[_Iterable[str]] = ...) -> None: ...

class CognitiveMetricsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CognitiveMetricsResponse(_message.Message):
    __slots__ = ("total_nodes", "fallbacks", "identity", "constraint", "decision", "fact", "preference", "episode", "tier_hard", "tier_soft", "tier_variant", "heading_identity", "heading_constraint", "heading_workflow", "heading_background", "heading_preferences", "support_buckets", "circuit_open", "circuit_reason", "use_cognitive_routing")
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    FALLBACKS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    DECISION_FIELD_NUMBER: _ClassVar[int]
    FACT_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_FIELD_NUMBER: _ClassVar[int]
    EPISODE_FIELD_NUMBER: _ClassVar[int]
    TIER_HARD_FIELD_NUMBER: _ClassVar[int]
    TIER_SOFT_FIELD_NUMBER: _ClassVar[int]
    TIER_VARIANT_FIELD_NUMBER: _ClassVar[int]
    HEADING_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    HEADING_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    HEADING_WORKFLOW_FIELD_NUMBER: _ClassVar[int]
    HEADING_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    HEADING_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SUPPORT_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_OPEN_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_REASON_FIELD_NUMBER: _ClassVar[int]
    USE_COGNITIVE_ROUTING_FIELD_NUMBER: _ClassVar[int]
    total_nodes: int
    fallbacks: int
    identity: int
    constraint: int
    decision: int
    fact: int
    preference: int
    episode: int
    tier_hard: int
    tier_soft: int
    tier_variant: int
    heading_identity: int
    heading_constraint: int
    heading_workflow: int
    heading_background: int
    heading_preferences: int
    support_buckets: _containers.RepeatedScalarFieldContainer[int]
    circuit_open: bool
    circuit_reason: str
    use_cognitive_routing: bool
    def __init__(self, total_nodes: _Optional[int] = ..., fallbacks: _Optional[int] = ..., identity: _Optional[int] = ..., constraint: _Optional[int] = ..., decision: _Optional[int] = ..., fact: _Optional[int] = ..., preference: _Optional[int] = ..., episode: _Optional[int] = ..., tier_hard: _Optional[int] = ..., tier_soft: _Optional[int] = ..., tier_variant: _Optional[int] = ..., heading_identity: _Optional[int] = ..., heading_constraint: _Optional[int] = ..., heading_workflow: _Optional[int] = ..., heading_background: _Optional[int] = ..., heading_preferences: _Optional[int] = ..., support_buckets: _Optional[_Iterable[int]] = ..., circuit_open: bool = ..., circuit_reason: _Optional[str] = ..., use_cognitive_routing: bool = ...) -> None: ...

class ReindexChange(_message.Message):
    __slots__ = ("ordinal", "kind", "text_preview", "legacy_tier", "cognitive_tier", "memory_kind", "memory_support", "memory_role", "tier_changed")
    ORDINAL_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    TEXT_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    LEGACY_TIER_FIELD_NUMBER: _ClassVar[int]
    COGNITIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    MEMORY_KIND_FIELD_NUMBER: _ClassVar[int]
    MEMORY_SUPPORT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_ROLE_FIELD_NUMBER: _ClassVar[int]
    TIER_CHANGED_FIELD_NUMBER: _ClassVar[int]
    ordinal: int
    kind: str
    text_preview: str
    legacy_tier: int
    cognitive_tier: int
    memory_kind: str
    memory_support: float
    memory_role: str
    tier_changed: bool
    def __init__(self, ordinal: _Optional[int] = ..., kind: _Optional[str] = ..., text_preview: _Optional[str] = ..., legacy_tier: _Optional[int] = ..., cognitive_tier: _Optional[int] = ..., memory_kind: _Optional[str] = ..., memory_support: _Optional[float] = ..., memory_role: _Optional[str] = ..., tier_changed: bool = ...) -> None: ...

class ReindexDryRunResult(_message.Message):
    __slots__ = ("total_nodes", "promote_tier", "changes")
    TOTAL_NODES_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_TIER_FIELD_NUMBER: _ClassVar[int]
    CHANGES_FIELD_NUMBER: _ClassVar[int]
    total_nodes: int
    promote_tier: bool
    changes: _containers.RepeatedCompositeFieldContainer[ReindexChange]
    def __init__(self, total_nodes: _Optional[int] = ..., promote_tier: bool = ..., changes: _Optional[_Iterable[_Union[ReindexChange, _Mapping]]] = ...) -> None: ...

class ReindexLiveResult(_message.Message):
    __slots__ = ("ok", "promote_cognitive_tier", "nodes_accepted", "nodes_rejected", "tokens_ingested")
    OK_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_COGNITIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    NODES_ACCEPTED_FIELD_NUMBER: _ClassVar[int]
    NODES_REJECTED_FIELD_NUMBER: _ClassVar[int]
    TOKENS_INGESTED_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    promote_cognitive_tier: bool
    nodes_accepted: int
    nodes_rejected: int
    tokens_ingested: int
    def __init__(self, ok: bool = ..., promote_cognitive_tier: bool = ..., nodes_accepted: _Optional[int] = ..., nodes_rejected: _Optional[int] = ..., tokens_ingested: _Optional[int] = ...) -> None: ...

class ReindexAuthoredDocumentRequest(_message.Message):
    __slots__ = ("source_doc", "text", "tokenizer_id", "core_doc", "source_meta", "promote_cognitive_tier", "dry_run")
    SOURCE_DOC_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TOKENIZER_ID_FIELD_NUMBER: _ClassVar[int]
    CORE_DOC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_META_FIELD_NUMBER: _ClassVar[int]
    PROMOTE_COGNITIVE_TIER_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    source_doc: str
    text: str
    tokenizer_id: str
    core_doc: bool
    source_meta: MarkdownSourceMeta
    promote_cognitive_tier: bool
    dry_run: bool
    def __init__(self, source_doc: _Optional[str] = ..., text: _Optional[str] = ..., tokenizer_id: _Optional[str] = ..., core_doc: bool = ..., source_meta: _Optional[_Union[MarkdownSourceMeta, _Mapping]] = ..., promote_cognitive_tier: bool = ..., dry_run: bool = ...) -> None: ...

class ReindexAuthoredDocumentResponse(_message.Message):
    __slots__ = ("source_doc", "dry_run", "live")
    SOURCE_DOC_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    LIVE_FIELD_NUMBER: _ClassVar[int]
    source_doc: str
    dry_run: ReindexDryRunResult
    live: ReindexLiveResult
    def __init__(self, source_doc: _Optional[str] = ..., dry_run: _Optional[_Union[ReindexDryRunResult, _Mapping]] = ..., live: _Optional[_Union[ReindexLiveResult, _Mapping]] = ...) -> None: ...

class MarkMemorySupersededRequest(_message.Message):
    __slots__ = ("collection", "old_id", "new_id", "valid_until")
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    OLD_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_ID_FIELD_NUMBER: _ClassVar[int]
    VALID_UNTIL_FIELD_NUMBER: _ClassVar[int]
    collection: str
    old_id: str
    new_id: str
    valid_until: int
    def __init__(self, collection: _Optional[str] = ..., old_id: _Optional[str] = ..., new_id: _Optional[str] = ..., valid_until: _Optional[int] = ...) -> None: ...

class MarkMemorySupersededResponse(_message.Message):
    __slots__ = ("ok",)
    OK_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    def __init__(self, ok: bool = ...) -> None: ...

class HealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MemoryStatusRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FlushRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListLifecycleJournalResponse(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, entries: _Optional[_Iterable[str]] = ...) -> None: ...

class ListCollectionResponse(_message.Message):
    __slots__ = ("ids",)
    IDS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ListByMetaResponse(_message.Message):
    __slots__ = ("results",)
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    def __init__(self, results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]] = ...) -> None: ...

class ExpandSummaryResponse(_message.Message):
    __slots__ = ("summary_id", "text")
    SUMMARY_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    summary_id: str
    text: str
    def __init__(self, summary_id: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...

class QueryRawSessionResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[KernelMessage]
    def __init__(self, messages: _Optional[_Iterable[_Union[KernelMessage, _Mapping]]] = ...) -> None: ...
