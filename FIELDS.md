# AssembleConfigOverrides — Canonical Field Registry

**Contract:** `proto/libravdb/ipc/v1/rpc.proto` — `AssembleConfigOverrides` message

**Status:** Active, flat message. **No oneof. No alternate override message.**

**Source of truth for daemon handlers:** `kernel_handlers.go` in the libravdb daemon repo.

**Plugin camelCase ↔ proto snake_case:** Standard protobuf conventions, no custom serialization.

---

## Field Registry

| Field # | snake_case proto name | camelCase plugin name | Type | Daemon Handler | Status | Notes |
|---------|----------------------|---------------------|------|---------------|--------|-------|
| 1 | use_session_recall_projection | useSessionRecallProjection | bool | LIVE | Active | |
| 2 | use_session_summary_search_experiment | useSessionSummarySearchExperiment | bool | LIVE | Active | |
| 3 | token_budget_fraction | tokenBudgetFraction | double | LIVE | Active | |
| 4 | authored_hard_budget_fraction | authoredHardBudgetFraction | double | LIVE | Active | |
| 5 | authored_soft_budget_fraction | authoredSoftBudgetFraction | double | LIVE | Active | |
| 6 | elevated_guidance_budget_fraction | elevatedGuidanceBudgetFraction | double | LIVE | Active | |
| 7 | top_k | topK | int32 | LIVE | Active | |
| 8 | continuity_min_turns | continuityMinTurns | int32 | LIVE | Active | |
| 9 | continuity_tail_budget_tokens | continuityTailBudgetTokens | int32 | LIVE | Active | |
| 10 | continuity_prior_context_tokens | continuityPriorContextTokens | int32 | LIVE | Active | |
| **11** | **compact_threshold** | **compactThreshold** | **int32** | **NONE** | **DEPRECATED** | No daemon handler. Was used for compaction tuning; daemon now derives internally from token budget signals. Do not use until wired. |
| 12 | compact_session_token_budget | compactSessionTokenBudget | int32 | LIVE | Active | |
| 13 | section7_theta1 | section7Theta1 | double | LIVE | Active | |
| 14 | section7_kappa | section7Kappa | double | LIVE | Active | |
| 15 | section7_hop_eta | section7HopEta | double | LIVE | Active | |
| 16 | section7_hop_threshold | section7HopThreshold | double | LIVE | Active | |
| 17 | section7_coarse_top_k | section7CoarseTopK | int32 | LIVE | Active | |
| 18 | section7_second_pass_top_k | section7SecondPassTopK | int32 | LIVE | Active | |
| **19** | **section7_authority_recency_lambda** | **section7AuthorityRecencyLambda** | **double** | **NONE** | **DEPRECATED** | Latent authority signal never connected to ranking pipeline. Do not use until wired. |
| 20 | section7_authority_recency_weight | section7AuthorityRecencyWeight | double | LIVE | Active | |
| 21 | section7_authority_frequency_weight | section7AuthorityFrequencyWeight | double | LIVE | Active | |
| 22 | section7_authority_authored_weight | section7AuthorityAuthoredWeight | double | LIVE | Active | |
| 23 | recovery_floor_score | recoveryFloorScore | double | LIVE | Active | |
| 24 | recovery_min_top_k | recoveryMinTopK | int32 | LIVE | Active | |
| 25 | recovery_min_confidence_mean | recoveryMinConfidenceMean | double | LIVE | Active | |
| **26** | **recency_lambda_session** | **recencyLambdaSession** | **double** | **NONE** | **DEPRECATED** | Reserved for session-scoped recency weighting; no active daemon handler. Do not use until wired. |
| 27 | recency_lambda_user | recencyLambdaUser | double | LIVE | Active | |
| **28** | **recency_lambda_global** | **recencyLambdaGlobal** | **double** | **NONE** | **DEPRECATED** | Reserved for global recency weighting; no active daemon handler. Do not use until wired. |
| 29 | ingestion_gate_threshold | ingestionGateThreshold | double | LIVE | Active | |
| 30 | section7_authority_salience_weight | section7AuthoritySalienceWeight | double | LIVE | Active | Plugin PR #160 adding |
| 31 | section7_recency_access_lambda | section7RecencyAccessLambda | double | LIVE | Active | Plugin PR #160 adding |

---

## Ghost Keys — NOT in Contract

The following exist in the TS plugin but have **no proto counterpart**. They are TS-sidecar drift from when the daemon was TypeScript. **Must NOT be added to `AssembleConfigOverrides` without an explicit daemon implementation decision.**

| Plugin camelCase name | Status |
|----------------------|--------|
| section7StartupTokenBudgetTokens | NOT in proto — ghost key |
| summaryExpansionConfidenceThreshold | NOT in proto — ghost key |
| summaryExpansionDepth | NOT in proto — ghost key |
| summaryExpansionTokenBudget | NOT in proto — ghost key |
| summaryExpansionPenaltyFactor | NOT in proto — ghost key |

---

## Field Numbering

Field numbers 1–31 are all assigned. Non-sequential ordering (23–29 followed by 30, 31) is **intentional reservation** — these slots were held for potential future fields. Field numbers 32+ are available for future use. Do not reassign existing field numbers.

| Range | Status |
|-------|--------|
| 1–10 | Active fields |
| 11 | DEPRECATED — reserved, not removed |
| 12–18 | Active fields |
| 19 | DEPRECATED — reserved, not removed |
| 20–22 | Active fields |
| 23–25 | Active fields |
| 26 | DEPRECATED — reserved, not removed |
| 27 | Active field |
| 28 | DEPRECATED — reserved, not removed |
| 29 | Active field |
| 30–31 | Active fields (plugin PR #160) |
| 32+ | Available for future use |

---

## Deprecation Policy

Fields marked DEPRECATED (11, 19, 26, 28) must **not** be removed from proto. Removing proto fields breaks wire compatibility if any client is sending them.

**Before removal**, the following must be confirmed:
1. No active plugin client sends these fields
2. Daemon logs a warning when consumed (to catch any stray traffic)
3. A major version bump is planned

---

## Canonical Statement

> `AssembleConfigOverrides` is the single canonical override message for the libravdb IPC contract. No alternate message exists in this contract. The five ghost keys (`section7StartupTokenBudgetTokens`, `summaryExpansionConfidenceThreshold`, `summaryExpansionDepth`, `summaryExpansionTokenBudget`, `summaryExpansionPenaltyFactor`) are TS-sidecar artifacts and are not part of this contract.