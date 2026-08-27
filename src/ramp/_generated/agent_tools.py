"""Generated Ramp Python SDK surface; do not edit by hand.

Source spec SHA-256: 3e6ddcad1afacc297dc867067bbccf3641d78d914582f073d488fd65ade34a45
Overlay SHA-256: d5f3ef06254a037e235f662345d95093b60c900e56b6eec8449a6dad396e922b
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any, TypeAlias, cast
from uuid import UUID

from ramp._types import (
    NOT_GIVEN,
    AsyncTransport,
    FileInput,
    NotGiven,
    OperationMetadata,
    SyncTransport,
)

# Response names are sourced from the IR. Full Pydantic model rendering
# remains separate from resource and method generation.
AddUserToSharedFundPublicResult: TypeAlias = dict[str, Any]
Agent: TypeAlias = dict[str, Any]
AgentCardFundsList: TypeAlias = dict[str, Any]
AgentCreateResponse: TypeAlias = dict[str, Any]
AgentCredentials: TypeAlias = dict[str, Any]
AgentWalletPolicyListResponse: TypeAlias = dict[str, Any]
AggregatedUsageResponseSchema: TypeAlias = dict[str, Any]
AiCurrentSpendResponseSchema: TypeAlias = dict[str, Any]
AiTokenSpendAggregatesResult: TypeAlias = dict[str, Any]
AiTokenSpendConnectionsResult: TypeAlias = dict[str, Any]
AiTokenSpendFilterOptionsResult: TypeAlias = dict[str, Any]
ApiApplicationDocumentResource: TypeAlias = dict[str, Any]
ApiApplicationProgressResource: TypeAlias = dict[str, Any]
ApiApplicationResource: TypeAlias = dict[str, Any]
ApiBankAccountResource: TypeAlias = dict[str, Any]
ApiFollowupListResource: TypeAlias = dict[str, Any]
ApiFollowupResource: TypeAlias = dict[str, Any]
ApiRolesList: TypeAlias = dict[str, Any]
ApiSourcingUploadDocumentResultJsonMode: TypeAlias = dict[str, Any]
ArchiveSpendAllocationOutput: TypeAlias = dict[str, Any]
AskRampExternalResult: TypeAlias = dict[str, Any]
AttachReceiptSuccess: TypeAlias = dict[str, Any]
AttachVendorDocumentResult: TypeAlias = dict[str, Any]
AwardSourcingEventOutput: TypeAlias = dict[str, Any]
BillActionResult: TypeAlias = dict[str, Any]
BillApproverReminderResult: TypeAlias = dict[str, Any]
BillCommentsResult: TypeAlias = dict[str, Any]
BillDetails: TypeAlias = dict[str, Any]
BillHistoryResult: TypeAlias = dict[str, Any]
BillInvoicesResult: TypeAlias = dict[str, Any]
BillSearchResult: TypeAlias = dict[str, Any]
BillStatus: TypeAlias = dict[str, Any]
BookingDetails: TypeAlias = dict[str, Any]
BookingsResult: TypeAlias = dict[str, Any]
BulkClosePurchaseOrdersResult: TypeAlias = dict[str, Any]
BulkReopenPurchaseOrdersResult: TypeAlias = dict[str, Any]
BulkUploadVendorDocumentsResult: TypeAlias = dict[str, Any]
BusinessStatementDateResponse: TypeAlias = dict[str, Any]
CancelReimbursementPaymentSuccess: TypeAlias = dict[str, Any]
CandidateTripsResult: TypeAlias = dict[str, Any]
CardActivationResult: TypeAlias = dict[str, Any]
CardInfoList: TypeAlias = dict[str, Any]
CardLockResult: TypeAlias = dict[str, Any]
CardStatementBalanceJsonMode: TypeAlias = dict[str, Any]
CardUnlockResult: TypeAlias = dict[str, Any]
CloseSourcingEventOutput: TypeAlias = dict[str, Any]
CommentPosted: TypeAlias = dict[str, Any]
CompleteTransactionRevisionResult: TypeAlias = dict[str, Any]
CreateDepartmentOutput: TypeAlias = dict[str, Any]
CreateDraftBillResult: TypeAlias = dict[str, Any]
CreateDraftPayeeResult: TypeAlias = dict[str, Any]
CreateDraftSpendRequestFromSourcingEventOutput: TypeAlias = dict[str, Any]
CreateRFXOutput: TypeAlias = dict[str, Any]
DeclineExplanation: TypeAlias = dict[str, Any]
DeleteReimbursementSuccess: TypeAlias = dict[str, Any]
DeleteSpendProgramResult: TypeAlias = dict[str, Any]
DeletedProcurementDraft: TypeAlias = dict[str, Any]
DraftBillDetails: TypeAlias = dict[str, Any]
DrawdownRequestResponse: TypeAlias = dict[str, Any]
DuplicateReimbursementSuccess: TypeAlias = dict[str, Any]
EditReimbursementSuccess: TypeAlias = dict[str, Any]
EditTransactionSuccess: TypeAlias = dict[str, Any]
EditUserRoleOnSharedFundPublicResult: TypeAlias = dict[str, Any]
EmployeeSubmissionPolicyRequirementsSuccess: TypeAlias = dict[str, Any]
EmptyObject: TypeAlias = dict[str, Any]
EnableSharedFundAccessResult: TypeAlias = dict[str, Any]
EstimateMileageReimbursementResult: TypeAlias = dict[str, Any]
EstimatePerDiemAmountSuccess: TypeAlias = dict[str, Any]
FlightBookingResult: TypeAlias = dict[str, Any]
FlightCancellationResponse: TypeAlias = dict[str, Any]
FlightLocationSearchResult: TypeAlias = dict[str, Any]
FullTransactionMetadata: TypeAlias = dict[str, Any]
FundRequestLink: TypeAlias = dict[str, Any]
FundX402WalletResult: TypeAlias = dict[str, Any]
GetAccountBalanceHistoryOutput: TypeAlias = dict[str, Any]
GetAllReducedUsersResult: TypeAlias = dict[str, Any]
GetAttentionFeedResult: TypeAlias = dict[str, Any]
GetBillAmountSummaryResult: TypeAlias = dict[str, Any]
GetBillMetricsResult: TypeAlias = dict[str, Any]
GetExpenseWorkflowContextSuccess: TypeAlias = dict[str, Any]
GetHotelRatesResult: TypeAlias = dict[str, Any]
GetInvestmentAccountBalanceOutput: TypeAlias = dict[str, Any]
GetLatestSyncResponse: TypeAlias = dict[str, Any]
GetManagedPortfolioAccountBalanceOutput: TypeAlias = dict[str, Any]
GetMissingItemsByUserResult: TypeAlias = dict[str, Any]
GetMoreToolsResult: TypeAlias = dict[str, Any]
GetOfficeLocationsResult: TypeAlias = dict[str, Any]
GetOutstandingReimbursementsSuccess: TypeAlias = dict[str, Any]
GetPolicyWorkflowBodyPublicSuccess: TypeAlias = dict[str, Any]
GetRFXDetailOutput: TypeAlias = dict[str, Any]
GetRFXGradingOverviewOutput: TypeAlias = dict[str, Any]
GetRFXResponseSummaryOutput: TypeAlias = dict[str, Any]
GetRampBusinessAccountBalanceOutput: TypeAlias = dict[str, Any]
GetReimbursementReceiptsSuccess: TypeAlias = dict[str, Any]
GetReimbursementsResult: TypeAlias = dict[str, Any]
GetSourcingEventContextOutput: TypeAlias = dict[str, Any]
GetSyncCommitFailureDetailsResult: TypeAlias = dict[str, Any]
GetTrackingCategoriesResult: TypeAlias = dict[str, Any]
GetTrackingCategoryOptionsResult: TypeAlias = dict[str, Any]
GetTransactionsResult: TypeAlias = dict[str, Any]
GetTravelerProfileResult: TypeAlias = dict[str, Any]
GetTreasuryBalanceHistoryOutput: TypeAlias = dict[str, Any]
GetVendorAgreementPublicResult: TypeAlias = dict[str, Any]
GetVendorDocumentBulkStatusResult: TypeAlias = dict[str, Any]
HotelBookingResult: TypeAlias = dict[str, Any]
HotelCancellationResponse: TypeAlias = dict[str, Any]
InviteVendorsToRFXOutput: TypeAlias = dict[str, Any]
IssueFromSpendProgramResult: TypeAlias = dict[str, Any]
IssueOneOffFundsResult: TypeAlias = dict[str, Any]
LimitIncreaseResult: TypeAlias = dict[str, Any]
ListBusinessAccountsOutput: TypeAlias = dict[str, Any]
ListDepartmentsOutput: TypeAlias = dict[str, Any]
ListPoliciesSuccess: TypeAlias = dict[str, Any]
ListProcurementSpendIntentsResult: TypeAlias = dict[str, Any]
ListSkCategoriesResult: TypeAlias = dict[str, Any]
ListSourcingEventsOutput: TypeAlias = dict[str, Any]
ListTravelerLoyaltyProgramsResult: TypeAlias = dict[str, Any]
ListTreasuryAccountsOutput: TypeAlias = dict[str, Any]
ListVendorAgreementsResult: TypeAlias = dict[str, Any]
ListWalletTransfersOutput: TypeAlias = dict[str, Any]
LockOrUnlockSpendAllocationMemberResult: TypeAlias = dict[str, Any]
LockOrUnlockSpendAllocationResult: TypeAlias = dict[str, Any]
ManageRFXCollaboratorsOutput: TypeAlias = dict[str, Any]
MarkRFXGradedOutput: TypeAlias = dict[str, Any]
MarkTransactionMissingReceiptResponse: TypeAlias = dict[str, Any]
OrgChartResponse: TypeAlias = dict[str, Any]
PaginatedResponseAgentAccountNumberResponse: TypeAlias = dict[str, Any]
PaginatedResponseAgentSchema: TypeAlias = dict[str, Any]
PaginatedResponseApiApplicationDocumentResource: TypeAlias = dict[str, Any]
PaginatedResponseApiBankAccountResource: TypeAlias = dict[str, Any]
PaginatedResponseApiMerchantResourceSchema: TypeAlias = dict[str, Any]
PaginatedResponseApiStatementResourceSchema: TypeAlias = dict[str, Any]
PatchProvisionalBillResult: TypeAlias = dict[str, Any]
PaymentTokenResult: TypeAlias = dict[str, Any]
PolicyAnswer: TypeAlias = dict[str, Any]
PolicyDetailsSuccess: TypeAlias = dict[str, Any]
ProcurementDraftState: TypeAlias = dict[str, Any]
ProcurementSubmittedRequest: TypeAlias = dict[str, Any]
ProcurementUploadedFileResultJsonMode: TypeAlias = dict[str, Any]
ProvideNoReceiptReasonResponse: TypeAlias = dict[str, Any]
PublicAnalystCatalogResponse: TypeAlias = dict[str, Any]
PublicAnalystMetricMetadataResponse: TypeAlias = dict[str, Any]
PublicAnalystQueryResponse: TypeAlias = dict[str, Any]
PublicAnalystTableDomainDocsResponse: TypeAlias = dict[str, Any]
PublishRFXOutput: TypeAlias = dict[str, Any]
PurchaseOrderDetails: TypeAlias = dict[str, Any]
PurchaseOrderSearchResult: TypeAlias = dict[str, Any]
RFXVendorResponsesOutput: TypeAlias = dict[str, Any]
ReceiptUploadSuccess: TypeAlias = dict[str, Any]
RecentReimbursements: TypeAlias = dict[str, Any]
RecurringBillDetails: TypeAlias = dict[str, Any]
ReimbursementActionResult: TypeAlias = dict[str, Any]
ReimbursementCreationSuccess: TypeAlias = dict[str, Any]
ReimbursementsForApproval: TypeAlias = dict[str, Any]
RemoveTravelerLoyaltyProgramResult: TypeAlias = dict[str, Any]
RemoveUserFromSharedFundPublicResult: TypeAlias = dict[str, Any]
RenameDepartmentOutput: TypeAlias = dict[str, Any]
RepaymentRequestResult: TypeAlias = dict[str, Any]
ResubmitReimbursementSuccess: TypeAlias = dict[str, Any]
ReturnRFXToDraftOutput: TypeAlias = dict[str, Any]
RevokeRFXVendorInvitationOutput: TypeAlias = dict[str, Any]
SearchFlightsResult: TypeAlias = dict[str, Any]
SearchHelpCenterOutput: TypeAlias = dict[str, Any]
SearchHotelsResult: TypeAlias = dict[str, Any]
SearchMerchantsResult: TypeAlias = dict[str, Any]
SearchReimbursementsResult: TypeAlias = dict[str, Any]
SearchUserResponse: TypeAlias = dict[str, Any]
SearchVendorsResult: TypeAlias = dict[str, Any]
SendRFXResponseReminderOutput: TypeAlias = dict[str, Any]
SetDeclineBufferResult: TypeAlias = dict[str, Any]
SetRFXCoverSheetOutput: TypeAlias = dict[str, Any]
SetRFXPricingSheetOutput: TypeAlias = dict[str, Any]
SetRFXVendorInvitationContactOutput: TypeAlias = dict[str, Any]
SetTravelerLoyaltyProgramResult: TypeAlias = dict[str, Any]
SimplifiedUserDetailResponse: TypeAlias = dict[str, Any]
SimulatePolicyWorkflowForExpenseSuccess: TypeAlias = dict[str, Any]
SingleTransaction: TypeAlias = dict[str, Any]
Statement: TypeAlias = dict[str, Any]
SubmitAgentNpsResult: TypeAlias = dict[str, Any]
SubmitDraftBillResult: TypeAlias = dict[str, Any]
SubmitReimbursementSuccess: TypeAlias = dict[str, Any]
SuggestedMemos: TypeAlias = dict[str, Any]
ToolStringOutput: TypeAlias = dict[str, Any]
TransactionActionResult: TypeAlias = dict[str, Any]
TransactionMissingItems: TypeAlias = dict[str, Any]
TransferSpendAllocationOwnershipPublicResult: TypeAlias = dict[str, Any]
TravelRequestActionResult: TypeAlias = dict[str, Any]
TravelRequestListResult: TypeAlias = dict[str, Any]
TravelerLoyaltyProgramCompatibilityResult: TypeAlias = dict[str, Any]
TripCreationResult: TypeAlias = dict[str, Any]
TripListResult: TypeAlias = dict[str, Any]
UnarchiveSpendAllocationOutput: TypeAlias = dict[str, Any]
UnifiedRequestActionResult: TypeAlias = dict[str, Any]
UnifiedRequestDetailsOutput: TypeAlias = dict[str, Any]
UnifiedRequestListResult: TypeAlias = dict[str, Any]
UpdateCategoryRestrictionsResult: TypeAlias = dict[str, Any]
UpdateMerchantRestrictionsResult: TypeAlias = dict[str, Any]
UpdateRFXOutput: TypeAlias = dict[str, Any]
UpdateSpendAllocationIntervalOutput: TypeAlias = dict[str, Any]
UpdateTransactionAmountLimitResult: TypeAlias = dict[str, Any]
UpdateTravelerProfileResult: TypeAlias = dict[str, Any]
UserFunds: TypeAlias = dict[str, Any]
WithdrawX402WalletResult: TypeAlias = dict[str, Any]
X402PaymentSigned: TypeAlias = dict[str, Any]
X402WalletReady: TypeAlias = dict[str, Any]


_AGENT_TOOLS_PROCUREMENT_REQUESTS_DELETE_METADATA = OperationMetadata(
    operation_id="delete_agent_tool_api___delete_procurement_draft",
    scopes=("spend_requests:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_DEVELOPER_API_AGENTS_DELETE_METADATA = OperationMetadata(
    operation_id="delete_agent_item_resource",
    scopes=("agents:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_APPLICATIONS_DELETE_DOCUMENT_METADATA = OperationMetadata(
    operation_id="delete_application_document_detail_resource",
    scopes=("applications:write",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_AGENT_TOOLS_TREASURY_BALANCE_HISTORY_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_account_balance_history",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BUSINESS_GET_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_business_statement_date_tool",
    scopes=("statements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_POLICY_REQUIREMENTS_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_employee_submission_policy_requirements",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_POLICY_EXPLAIN_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_expense_workflow_context",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_INVESTMENTS_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_investment_account_balance",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_PORTFOLIO_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_managed_portfolio_account_balance",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_MISSING_BY_USER_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_missing_items_by_user",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_POLICY_GET_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_policy_details",
    scopes=("workflows:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_POLICY_BODY_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_policy_workflow_body",
    scopes=("workflows:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_SUMMARY_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_ramp_business_account_balance",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_HISTORY_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_treasury_balance_history",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_VENDORS_BULK_UPLOAD_STATUS_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_vendor_document_bulk_status",
    scopes=("vendors:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_ACCOUNTS_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___list_business_accounts",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_POLICY_LIST_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___list_policies",
    scopes=("workflows:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_LIST_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___list_treasury_accounts",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TREASURY_TRANSFERS_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___list_wallet_transfers",
    scopes=("treasury:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_PROCUREMENT_REQUESTS_GET_METADATA = OperationMetadata(
    operation_id="get_agent_tool_api___get_procurement_draft",
    scopes=("spend_requests:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_DEVELOPER_API_AGENT_WALLET_LIST_METADATA = OperationMetadata(
    operation_id="get_agent_wallet_policy_publication_resource",
    scopes=("agent_wallet_policy:read",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="agent_wallet_enabled",
)


_DEVELOPER_API_AGENTS_LIST_METADATA = OperationMetadata(
    operation_id="get_agent_list_resource",
    scopes=("agents:read",),
    platforms=("cli",),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_AGENTS_GET_METADATA = OperationMetadata(
    operation_id="get_agent_item_resource",
    scopes=("agents:read",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_APPLICATIONS_GET_METADATA = OperationMetadata(
    operation_id="get_application_resource",
    scopes=("applications:read",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_DEVELOPER_API_APPLICATIONS_DOCUMENTS_METADATA = OperationMetadata(
    operation_id="get_application_document_resource",
    scopes=("applications:read",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_APPLICATIONS_FOLLOWUPS_METADATA = OperationMetadata(
    operation_id="get_application_followup_list_resource",
    scopes=("applications:read",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_APPLICATIONS_PROGRESS_METADATA = OperationMetadata(
    operation_id="get_application_progress_resource",
    scopes=("applications:read",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_ASK_RAMP_GET_RESULT_METADATA = OperationMetadata(
    operation_id="get_ask_ramp_session_result_resource",
    scopes=("ask_ramp:read",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_ask_ramp_enabled",
)


_DEVELOPER_API_BANK_LINK_ACCOUNTS_METADATA = OperationMetadata(
    operation_id="get_bank_account_list_with_pagination",
    scopes=("bank_accounts:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_TREASURY_ACCOUNT_NUMBERS_METADATA = OperationMetadata(
    operation_id="get_agent_account_numbers_list_resource",
    scopes=("agent_account_numbers:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_MERCHANT_LIST_METADATA = OperationMetadata(
    operation_id="get_merchant_list_with_pagination",
    scopes=("merchants:read",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate=None,
)


_DEVELOPER_API_USERS_ROLES_METADATA = OperationMetadata(
    operation_id="get_roles_resource",
    scopes=("users:read",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_DEVELOPER_API_STATEMENTS_LIST_METADATA = OperationMetadata(
    operation_id="get_statement_list_with_pagination",
    scopes=("statements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="query_cursor",
    safety="read_only",
    gate=None,
)


_DEVELOPER_API_STATEMENTS_GET_METADATA = OperationMetadata(
    operation_id="get_statement_resource",
    scopes=("statements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_DEVELOPER_API_AGENTS_UPDATE_METADATA = OperationMetadata(
    operation_id="patch_agent_item_resource",
    scopes=("agents:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_APPLICATIONS_EDIT_METADATA = OperationMetadata(
    operation_id="patch_application_update_resource",
    scopes=("applications:write",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_APPLICATIONS_UPDATE_FOLLOWUP_METADATA = OperationMetadata(
    operation_id="patch_application_followup_resource",
    scopes=("applications:write",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_TRANSACTIONS_SPLIT_METADATA = OperationMetadata(
    operation_id="patch_transaction_canonical_update_resource",
    scopes=("transactions:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate=None,
)


_DEVELOPER_API_ACCOUNTING_MARK_READY_TO_SYNC_METADATA = OperationMetadata(
    operation_id="post_ready_to_sync_resource",
    scopes=("accounting:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_CARDS_ACTIVATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___activate_card",
    scopes=("cards:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_ADD_TRAVELER_LOYALTY_PROGRAM_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___traveler_loyalty_program_legacy_setter",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_FUNDS_ADD_USER_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___add_user_to_shared_fund",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_POLICY_POLICY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___answer_policy_question",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_APPROVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___approve_or_reject_bill",
    scopes=("bills:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_bill_pay_write_agent_tools_enabled",
)


_AGENT_TOOLS_REIMBURSEMENTS_APPROVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___approve_or_reject_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_REQUESTS_APPROVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___approve_or_reject_request",
    scopes=("approvals:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_APPROVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___approve_or_reject_transaction",
    scopes=("transactions:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_ARCHIVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___archive_spend_allocation_tool",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_RECEIPTS_ATTACH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___attach_receipt_to_transaction",
    scopes=("receipts:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_VENDORS_ATTACH_DOCUMENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___attach_vendor_document",
    scopes=("vendors:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_AWARD_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___award_sourcing_event",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_VENDORS_BULK_UPLOAD_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___bulk_upload_vendor_documents",
    scopes=("vendors:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_CANCEL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___cancel_reimbursement_payment",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_CLOSE_EVENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___close_sourcing_event",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_TRANSACTIONS_COMPLETE_REVISION_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___complete_transaction_revision",
    scopes=("transactions:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_BUSINESS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_department",
    scopes=("departments:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_BILLS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_draft_bill",
    scopes=("bills:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_bill_pay_write_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_DRAFT_SPEND_REQUEST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_draft_spend_request_from_sourcing_event",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_REQUEST_FUNDS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_fund_request",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_VENDORS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_pending_payee_direct",
    scopes=("vendors:read", "vendors:write"),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_pending_payee_agent_tool_enabled",
)


_AGENT_TOOLS_REIMBURSEMENTS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_reimbursement_from_receipt",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_rfx",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_TRAVEL_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___create_trip",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_DELETE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___delete_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate=None,
)


_AGENT_TOOLS_FUNDS_DELETE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___delete_spend_program",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_BUSINESS_DEPARTMENTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_departments",
    scopes=("departments:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_REIMBURSEMENTS_DUPLICATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___duplicate_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___edit_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___edit_transaction",
    scopes=("transactions:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_EDIT_USER_ROLE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___edit_user_role_on_shared_fund",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_FUNDS_ENABLE_SHARED_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___enable_shared_fund_access",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_AGENT_CARDS_ENROLL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___enroll_business_in_agent_cards",
    scopes=("cards:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___estimate_mileage_reimbursement",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_PER_DIEM_AMOUNT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___estimate_per_diem_amount",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_ANALYST_QUERY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___execute_analyst_query",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="mcp_core_analyst_tools_enabled",
)


_AGENT_TOOLS_X402_FUND_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___fund_x402_wallet",
    scopes=("x402:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_x402_enabled",
)


_AGENT_TOOLS_AGENT_CARDS_CREATE_PAYMENT_TOKEN_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_agent_card_creds",
    scopes=("cards:read_agentic",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_AGENT_CARDS_LIST_FUNDS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_agent_card_funds",
    scopes=("cards:read_agentic",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_AI_TOKEN_SPEND_AGGREGATES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_ai_token_spend_aggregates",
    scopes=("ai_spend:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_AI_TOKEN_SPEND_CONNECTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_ai_token_spend_connections",
    scopes=("ai_spend:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_AI_TOKEN_SPEND_CURRENT_SPEND_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_ai_token_spend_current_spend",
    scopes=("ai_spend:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_AI_TOKEN_SPEND_FILTER_OPTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_ai_token_spend_filter_options",
    scopes=("ai_spend:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_ANALYST_CATALOG_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_analyst_catalog",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="mcp_core_analyst_tools_enabled",
)


_AGENT_TOOLS_ANALYST_METRICS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_analyst_metric_metadata",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="mcp_core_analyst_tools_enabled",
)


_AGENT_TOOLS_ANALYST_SPEND_DOCS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_analyst_spend_facts_domain_docs",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="mcp_core_analyst_tools_enabled",
)


_AGENT_TOOLS_ANALYST_TABLE_DOCS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_analyst_table_domain_docs",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="mcp_core_analyst_tools_enabled",
)


_AGENT_TOOLS_TASKS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_attention_feed",
    scopes=("tasks:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_AMOUNT_SUMMARY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_amount_summary",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_COMMENTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_comments",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_GET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_details",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_HISTORY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_history",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_ATTACHMENTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_invoices",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_METRICS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_metrics",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_STATUS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bill_status",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_PENDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bills_for_approval",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_BOOKING_DETAILS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_booking_details",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="omni_travel_booking_support_skill_enabled",
)


_AGENT_TOOLS_TRAVEL_BOOKINGS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_bookings",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_TRIPS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_candidate_trips_for_transaction",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_STATEMENTS_OUTSTANDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_card_statement_balance",
    scopes=("statements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_DECLINES_EXPLAIN_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_decline_explanation",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_DRAFT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_draft_bill_details",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_LOCATIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_flight_booking_locations",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_GET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_full_transaction_metadata",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_FUNDS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_user_funds",
    scopes=("limits:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_HOTEL_RATES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_hotel_rates",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="ramp_cli_hotel_booking",
)


_AGENT_TOOLS_ACCOUNTING_LATEST_SYNC_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_latest_sync",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_EXTERNAL_AGENTS_GET_MORE_TOOLS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_more_tools",
    scopes=(),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_AI_TOKEN_SPEND_ME_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_my_ai_token_spend_aggregates",
    scopes=("ai_spend:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_OFFICES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_office_locations",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_USERS_ORG_CHART_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_org_chart",
    scopes=("users:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_OUTSTANDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_outstanding_reimbursements_by_currency",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_PENDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_pending_travel_requests",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate="travel_request_approvals_agent_tools_enabled",
)


_AGENT_TOOLS_PURCHASE_ORDERS_GET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_purchase_order_details",
    scopes=("purchase_orders:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_BILLS_RECURRING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_recurring_bill",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_RECEIPTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_reimbursement_receipts",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_reimbursements",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_PENDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_reimbursements_for_approval",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REQUESTS_PENDING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_requests_to_review",
    scopes=("unified_requests:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_SOURCING_RFX_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_rfx_detail",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_GRADING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_rfx_grading_overview",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_SUMMARY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_rfx_response_summary",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_RESPONSES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_rfx_vendor_responses",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_USERS_ME_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_simplified_user_detail",
    scopes=("users:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_SOURCING_EVENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_sourcing_event_context",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_ACCOUNTING_SYNC_FAILURES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_sync_commit_failure_details",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_ACCOUNTING_CATEGORIES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_tracking_categories",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_ACCOUNTING_CATEGORY_OPTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_tracking_category_options",
    scopes=("accounting:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_MISSING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_transaction_missing_items",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_MEMO_SUGGESTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_transaction_suggested_memos",
    scopes=("memos:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_user_transactions",
    scopes=("transactions:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_PROFILE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_traveler_profile",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REQUESTS_GET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_unified_request_details",
    scopes=("unified_requests:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_RECENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_user_recent_reimbursements",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_user_trips",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_VENDORS_GET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_vendor_agreement",
    scopes=("vendors:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_SOURCING_INVITE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___invite_vendors_to_rfx",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_ISSUE_FROM_PROGRAM_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___issue_from_spend_program",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="agent_fund_creation",
)


_AGENT_TOOLS_FUNDS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___issue_one_off_funds",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="agent_fund_creation",
)


_AGENT_TOOLS_FUNDS_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___limit_increase",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_BILLS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_bills",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_CARDS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_cards",
    scopes=("cards:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_SOURCING_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_sourcing_events",
    scopes=("sourcing:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAMS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_traveler_loyalty_programs",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_USERS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___get_all_reduced_users",
    scopes=("users:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_VENDORS_LIST_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_vendor_agreements",
    scopes=("vendors:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_CARDS_LOCK_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___lock_or_unlock_card",
    scopes=("cards:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_LOCK_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___lock_or_unlock_spend_allocation",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_LOCK_OR_UNLOCK_SPEND_ALLOCATION_MEMBER_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___lock_or_unlock_spend_allocation_member",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_COLLABORATORS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___manage_rfx_collaborators",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_MARK_GRADED_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___mark_rfx_graded",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_TRANSACTIONS_FLAG_MISSING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___mark_transaction_missing_receipt",
    scopes=("receipts:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_MERCHANT_CATEGORIES_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_sk_categories",
    scopes=("merchants:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_X402_PAY_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___pay_with_x402",
    scopes=("x402:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_x402_enabled",
)


_AGENT_TOOLS_COMMUNICATION_COMMENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___post_comment",
    scopes=("comments:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_PROCUREMENT_REQUESTS_DRAFT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___draft_procurement_request",
    scopes=("spend_requests:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_PROCUREMENT_REQUESTS_SPEND_INTENTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___list_procurement_spend_intents",
    scopes=("spend_requests:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_PROCUREMENT_REQUESTS_SUBMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_procurement_request",
    scopes=("spend_requests:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_PROCUREMENT_REQUESTS_UPLOAD_FILE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___upload_procurement_file",
    scopes=("spend_requests:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_TRANSACTIONS_EXPLAIN_MISSING_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___provide_no_receipt_reason",
    scopes=("receipts:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_X402_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___provision_x402_wallet",
    scopes=("x402_provisioning:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_x402_enabled",
)


_AGENT_TOOLS_SOURCING_PUBLISH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___publish_rfx",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_CLOSE_PURCHASE_ORDERS_METADATA = (
    OperationMetadata(
        operation_id="post_agent_tool_api___bulk_close_purchase_orders",
        scopes=("purchase_orders:write",),
        platforms=("cli", "mcp", "third_party"),
        stability="beta",
        pagination="none",
        safety="write",
        gate="mcp_purchase_order_lifecycle_tools_enabled",
    )
)


_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_REOPEN_PURCHASE_ORDERS_METADATA = (
    OperationMetadata(
        operation_id="post_agent_tool_api___bulk_reopen_purchase_orders",
        scopes=("purchase_orders:write",),
        platforms=("cli", "mcp", "third_party"),
        stability="beta",
        pagination="none",
        safety="write",
        gate="mcp_purchase_order_lifecycle_tools_enabled",
    )
)


_AGENT_TOOLS_BILLS_REMIND_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___remind_bill_approvers",
    scopes=("bills:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_bill_pay_write_agent_tools_enabled",
)


_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_REMOVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___remove_traveler_loyalty_program",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_FUNDS_REMOVE_USER_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___remove_user_from_shared_fund",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_BUSINESS_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___rename_department",
    scopes=("departments:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_REQUEST_REPAYMENT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___request_transaction_repayment",
    scopes=("transactions:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_RESUBMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___resubmit_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_RETURN_TO_DRAFT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___return_rfx_to_draft",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_REVOKE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___revoke_rfx_vendor_invitation",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_BILLS_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_bills",
    scopes=("bills:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_SEARCH_FLIGHT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_flights",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_RESEARCH_HELP_CENTER_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_help_center_snippets",
    scopes=(),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_SEARCH_HOTEL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_hotels",
    scopes=("trips:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate="ramp_cli_hotel_booking",
)


_AGENT_TOOLS_MERCHANT_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_merchants",
    scopes=("merchants:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate="developer_api_procurement_request_agent_tools_enabled",
)


_AGENT_TOOLS_PURCHASE_ORDERS_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_purchase_orders",
    scopes=("purchase_orders:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_REIMBURSEMENTS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_reimbursements",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REQUESTS_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_unified_requests",
    scopes=("unified_requests:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_TRANSACTIONS_SEARCH_SUGGESTED_USERS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___match_user_to_transaction",
    scopes=("users:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_user_reimbursements",
    scopes=("reimbursements:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="body_cursor",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_VENDORS_SEARCH_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___search_vendors",
    scopes=("vendors:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="read_only",
    gate=None,
)


_AGENT_TOOLS_SOURCING_REMIND_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___send_rfx_response_reminder",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_SET_DECLINE_BUFFER_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___set_decline_buffer",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_SOURCING_COVER_SHEET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___set_rfx_cover_sheet",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_PRICING_SHEET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___set_rfx_pricing_sheet",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_SOURCING_INVITATION_CONTACT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___set_rfx_vendor_invitation_contact",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_SET_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___set_traveler_loyalty_program",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_POLICY_SIMULATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___simulate_policy_workflow_for_expense",
    scopes=("workflows:read",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_BILLS_SUBMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_draft_bill",
    scopes=("bills:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_bill_pay_write_agent_tools_enabled",
)


_AGENT_TOOLS_TRAVEL_BOOK_FLIGHT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_flight_booking",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_TRAVEL_CANCEL_FLIGHT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_flight_cancellation",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="agent_booking_cancellation_enabled",
)


_AGENT_TOOLS_TRAVEL_BOOK_HOTEL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_hotel_booking",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="ramp_cli_hotel_booking",
)


_AGENT_TOOLS_TRAVEL_CANCEL_HOTEL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_hotel_cancellation",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="agent_booking_cancellation_enabled",
)


_AGENT_TOOLS_REIMBURSEMENTS_SUBMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_reimbursement",
    scopes=("reimbursements:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_GENERAL_AGENT_NPS_SUBMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___submit_agent_nps",
    scopes=(),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_TRANSFER_OWNERSHIP_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___transfer_spend_allocation_ownership",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_TRAVEL_APPROVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___travel_request_action",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="travel_request_approvals_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_UNARCHIVE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___unarchive_spend_allocation_tool",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_CARDS_UNLOCK_FRAUD_LOCKED_CARD_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___unlock_fraud_locked_card",
    scopes=("cards:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_FUNDS_UPDATE_CATEGORY_RESTRICTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_category_restrictions",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_BILLS_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___patch_provisional_bill",
    scopes=("bills:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_bill_pay_write_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_UPDATE_MERCHANT_RESTRICTIONS_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_merchant_restrictions",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_SOURCING_EDIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_rfx",
    scopes=("sourcing:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_FUNDS_UPDATE_INTERVAL_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_spend_allocation_interval_tool",
    scopes=("funds:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="spend_agent_tools",
)


_AGENT_TOOLS_FUNDS_UPDATE_TRANSACTION_AMOUNT_LIMIT_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_transaction_amount_limit",
    scopes=("limits:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_TRAVEL_UPDATE_TRAVELER_LOYALTY_PROGRAM_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___traveler_loyalty_program_number_setter",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="ramp_cli_flight_booking",
)


_AGENT_TOOLS_TRAVEL_PROFILE_UPDATE_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___update_traveler_profile",
    scopes=("trips:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_AGENT_TOOLS_RECEIPTS_UPLOAD_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___upload_receipt_file",
    scopes=("receipts:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate=None,
)


_DEVELOPER_API_SOURCING_UPLOAD_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___upload_sourcing_document",
    scopes=("sourcing:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_sourcing_agent_tools_enabled",
)


_AGENT_TOOLS_X402_WITHDRAW_METADATA = OperationMetadata(
    operation_id="post_agent_tool_api___withdraw_x402_wallet",
    scopes=("x402:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_x402_enabled",
)


_DEVELOPER_API_AGENT_WALLET_PUBLISH_POLICY_METADATA = OperationMetadata(
    operation_id="post_agent_wallet_policy_publication_resource",
    scopes=("agent_wallet_policy:write",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="agent_wallet_enabled",
)


_DEVELOPER_API_AGENTS_CREATE_METADATA = OperationMetadata(
    operation_id="post_agent_list_resource",
    scopes=("agents:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_AGENTS_ROTATE_SECRET_METADATA = OperationMetadata(
    operation_id="post_agent_rotate_secret_resource",
    scopes=("agents:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_AGENTS_SET_STATUS_METADATA = OperationMetadata(
    operation_id="post_agent_status_resource",
    scopes=("agents:write",),
    platforms=("cli",),
    stability="beta",
    pagination="none",
    safety="write",
    gate="identity_standalone_agents",
)


_DEVELOPER_API_APPLICATIONS_UPLOAD_METADATA = OperationMetadata(
    operation_id="post_application_document_resource",
    scopes=("applications:write",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_APPLICATIONS_SUBMIT_METADATA = OperationMetadata(
    operation_id="post_application_followup_submit_resource",
    scopes=("applications:write",),
    platforms=("cli", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_ASK_RAMP_ASK_METADATA = OperationMetadata(
    operation_id="post_ask_ramp_sessions_resource",
    scopes=("ask_ramp:read", "ask_ramp:write"),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_ask_ramp_enabled",
)


_DEVELOPER_API_ASK_RAMP_CONTINUE__METADATA = OperationMetadata(
    operation_id="post_ask_ramp_session_messages_resource",
    scopes=("ask_ramp:read",),
    platforms=("cli", "mcp"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_ask_ramp_enabled",
)


_DEVELOPER_API_BANK_LINK_CREATE_METADATA = OperationMetadata(
    operation_id="post_bank_account_create",
    scopes=("bank_accounts:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="write",
    gate="developer_api_agent_fa_enabled",
)


_DEVELOPER_API_TREASURY_REQUEST_FUNDS_METADATA = OperationMetadata(
    operation_id="post_banking_drawdown_requests_resource",
    scopes=("banking_drawdown_requests:write",),
    platforms=("cli", "mcp", "third_party"),
    stability="beta",
    pagination="none",
    safety="destructive",
    gate="developer_api_agent_fa_enabled",
)


OPERATION_METADATA = {
    "agent_tools.accounting.categories": _AGENT_TOOLS_ACCOUNTING_CATEGORIES_METADATA,
    "agent_tools.accounting.category_options": _AGENT_TOOLS_ACCOUNTING_CATEGORY_OPTIONS_METADATA,
    "agent_tools.accounting.latest_sync": _AGENT_TOOLS_ACCOUNTING_LATEST_SYNC_METADATA,
    "agent_tools.accounting.sync_failures": _AGENT_TOOLS_ACCOUNTING_SYNC_FAILURES_METADATA,
    "agent_tools.agent_cards.create_payment_token": _AGENT_TOOLS_AGENT_CARDS_CREATE_PAYMENT_TOKEN_METADATA,
    "agent_tools.agent_cards.enroll": _AGENT_TOOLS_AGENT_CARDS_ENROLL_METADATA,
    "agent_tools.agent_cards.list_funds": _AGENT_TOOLS_AGENT_CARDS_LIST_FUNDS_METADATA,
    "agent_tools.ai_token_spend.aggregates": _AGENT_TOOLS_AI_TOKEN_SPEND_AGGREGATES_METADATA,
    "agent_tools.ai_token_spend.connections": _AGENT_TOOLS_AI_TOKEN_SPEND_CONNECTIONS_METADATA,
    "agent_tools.ai_token_spend.current_spend": _AGENT_TOOLS_AI_TOKEN_SPEND_CURRENT_SPEND_METADATA,
    "agent_tools.ai_token_spend.filter_options": _AGENT_TOOLS_AI_TOKEN_SPEND_FILTER_OPTIONS_METADATA,
    "agent_tools.ai_token_spend.me": _AGENT_TOOLS_AI_TOKEN_SPEND_ME_METADATA,
    "agent_tools.analyst.catalog": _AGENT_TOOLS_ANALYST_CATALOG_METADATA,
    "agent_tools.analyst.metrics": _AGENT_TOOLS_ANALYST_METRICS_METADATA,
    "agent_tools.analyst.query": _AGENT_TOOLS_ANALYST_QUERY_METADATA,
    "agent_tools.analyst.spend_docs": _AGENT_TOOLS_ANALYST_SPEND_DOCS_METADATA,
    "agent_tools.analyst.table_docs": _AGENT_TOOLS_ANALYST_TABLE_DOCS_METADATA,
    "agent_tools.bills.amount_summary": _AGENT_TOOLS_BILLS_AMOUNT_SUMMARY_METADATA,
    "agent_tools.bills.approve": _AGENT_TOOLS_BILLS_APPROVE_METADATA,
    "agent_tools.bills.attachments": _AGENT_TOOLS_BILLS_ATTACHMENTS_METADATA,
    "agent_tools.bills.comments": _AGENT_TOOLS_BILLS_COMMENTS_METADATA,
    "agent_tools.bills.create": _AGENT_TOOLS_BILLS_CREATE_METADATA,
    "agent_tools.bills.draft": _AGENT_TOOLS_BILLS_DRAFT_METADATA,
    "agent_tools.bills.edit": _AGENT_TOOLS_BILLS_EDIT_METADATA,
    "agent_tools.bills.get": _AGENT_TOOLS_BILLS_GET_METADATA,
    "agent_tools.bills.history": _AGENT_TOOLS_BILLS_HISTORY_METADATA,
    "agent_tools.bills.list": _AGENT_TOOLS_BILLS_LIST_METADATA,
    "agent_tools.bills.metrics": _AGENT_TOOLS_BILLS_METRICS_METADATA,
    "agent_tools.bills.pending": _AGENT_TOOLS_BILLS_PENDING_METADATA,
    "agent_tools.bills.recurring": _AGENT_TOOLS_BILLS_RECURRING_METADATA,
    "agent_tools.bills.remind": _AGENT_TOOLS_BILLS_REMIND_METADATA,
    "agent_tools.bills.search": _AGENT_TOOLS_BILLS_SEARCH_METADATA,
    "agent_tools.bills.status": _AGENT_TOOLS_BILLS_STATUS_METADATA,
    "agent_tools.bills.submit": _AGENT_TOOLS_BILLS_SUBMIT_METADATA,
    "agent_tools.business.create": _AGENT_TOOLS_BUSINESS_CREATE_METADATA,
    "agent_tools.business.departments": _AGENT_TOOLS_BUSINESS_DEPARTMENTS_METADATA,
    "agent_tools.business.edit": _AGENT_TOOLS_BUSINESS_EDIT_METADATA,
    "agent_tools.business.get": _AGENT_TOOLS_BUSINESS_GET_METADATA,
    "agent_tools.cards.activate": _AGENT_TOOLS_CARDS_ACTIVATE_METADATA,
    "agent_tools.cards.list": _AGENT_TOOLS_CARDS_LIST_METADATA,
    "agent_tools.cards.lock": _AGENT_TOOLS_CARDS_LOCK_METADATA,
    "agent_tools.cards.unlock_fraud_locked_card": _AGENT_TOOLS_CARDS_UNLOCK_FRAUD_LOCKED_CARD_METADATA,
    "agent_tools.communication.comment": _AGENT_TOOLS_COMMUNICATION_COMMENT_METADATA,
    "agent_tools.declines.explain": _AGENT_TOOLS_DECLINES_EXPLAIN_METADATA,
    "agent_tools.external_agents.get_more_tools": _AGENT_TOOLS_EXTERNAL_AGENTS_GET_MORE_TOOLS_METADATA,
    "agent_tools.funds.add_user": _AGENT_TOOLS_FUNDS_ADD_USER_METADATA,
    "agent_tools.funds.archive": _AGENT_TOOLS_FUNDS_ARCHIVE_METADATA,
    "agent_tools.funds.create": _AGENT_TOOLS_FUNDS_CREATE_METADATA,
    "agent_tools.funds.delete": _AGENT_TOOLS_FUNDS_DELETE_METADATA,
    "agent_tools.funds.edit": _AGENT_TOOLS_FUNDS_EDIT_METADATA,
    "agent_tools.funds.edit_user_role": _AGENT_TOOLS_FUNDS_EDIT_USER_ROLE_METADATA,
    "agent_tools.funds.enable_shared": _AGENT_TOOLS_FUNDS_ENABLE_SHARED_METADATA,
    "agent_tools.funds.issue_from_program": _AGENT_TOOLS_FUNDS_ISSUE_FROM_PROGRAM_METADATA,
    "agent_tools.funds.list": _AGENT_TOOLS_FUNDS_LIST_METADATA,
    "agent_tools.funds.lock": _AGENT_TOOLS_FUNDS_LOCK_METADATA,
    "agent_tools.funds.lock_or_unlock_spend_allocation_member": _AGENT_TOOLS_FUNDS_LOCK_OR_UNLOCK_SPEND_ALLOCATION_MEMBER_METADATA,
    "agent_tools.funds.remove_user": _AGENT_TOOLS_FUNDS_REMOVE_USER_METADATA,
    "agent_tools.funds.request_funds": _AGENT_TOOLS_FUNDS_REQUEST_FUNDS_METADATA,
    "agent_tools.funds.set_decline_buffer": _AGENT_TOOLS_FUNDS_SET_DECLINE_BUFFER_METADATA,
    "agent_tools.funds.transfer_ownership": _AGENT_TOOLS_FUNDS_TRANSFER_OWNERSHIP_METADATA,
    "agent_tools.funds.unarchive": _AGENT_TOOLS_FUNDS_UNARCHIVE_METADATA,
    "agent_tools.funds.update_category_restrictions": _AGENT_TOOLS_FUNDS_UPDATE_CATEGORY_RESTRICTIONS_METADATA,
    "agent_tools.funds.update_interval": _AGENT_TOOLS_FUNDS_UPDATE_INTERVAL_METADATA,
    "agent_tools.funds.update_merchant_restrictions": _AGENT_TOOLS_FUNDS_UPDATE_MERCHANT_RESTRICTIONS_METADATA,
    "agent_tools.funds.update_transaction_amount_limit": _AGENT_TOOLS_FUNDS_UPDATE_TRANSACTION_AMOUNT_LIMIT_METADATA,
    "agent_tools.general.agent_nps_submit": _AGENT_TOOLS_GENERAL_AGENT_NPS_SUBMIT_METADATA,
    "agent_tools.merchant.categories": _AGENT_TOOLS_MERCHANT_CATEGORIES_METADATA,
    "agent_tools.merchant.search": _AGENT_TOOLS_MERCHANT_SEARCH_METADATA,
    "agent_tools.policy.body": _AGENT_TOOLS_POLICY_BODY_METADATA,
    "agent_tools.policy.explain": _AGENT_TOOLS_POLICY_EXPLAIN_METADATA,
    "agent_tools.policy.get": _AGENT_TOOLS_POLICY_GET_METADATA,
    "agent_tools.policy.list": _AGENT_TOOLS_POLICY_LIST_METADATA,
    "agent_tools.policy.policy": _AGENT_TOOLS_POLICY_POLICY_METADATA,
    "agent_tools.policy.requirements": _AGENT_TOOLS_POLICY_REQUIREMENTS_METADATA,
    "agent_tools.policy.simulate": _AGENT_TOOLS_POLICY_SIMULATE_METADATA,
    "agent_tools.procurement_requests.delete": _AGENT_TOOLS_PROCUREMENT_REQUESTS_DELETE_METADATA,
    "agent_tools.procurement_requests.draft": _AGENT_TOOLS_PROCUREMENT_REQUESTS_DRAFT_METADATA,
    "agent_tools.procurement_requests.get": _AGENT_TOOLS_PROCUREMENT_REQUESTS_GET_METADATA,
    "agent_tools.procurement_requests.spend_intents": _AGENT_TOOLS_PROCUREMENT_REQUESTS_SPEND_INTENTS_METADATA,
    "agent_tools.procurement_requests.submit": _AGENT_TOOLS_PROCUREMENT_REQUESTS_SUBMIT_METADATA,
    "agent_tools.procurement_requests.upload_file": _AGENT_TOOLS_PROCUREMENT_REQUESTS_UPLOAD_FILE_METADATA,
    "agent_tools.purchase_orders.get": _AGENT_TOOLS_PURCHASE_ORDERS_GET_METADATA,
    "agent_tools.purchase_orders.ramp_bulk_close_purchase_orders": _AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_CLOSE_PURCHASE_ORDERS_METADATA,
    "agent_tools.purchase_orders.ramp_bulk_reopen_purchase_orders": _AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_REOPEN_PURCHASE_ORDERS_METADATA,
    "agent_tools.purchase_orders.search": _AGENT_TOOLS_PURCHASE_ORDERS_SEARCH_METADATA,
    "agent_tools.receipts.attach": _AGENT_TOOLS_RECEIPTS_ATTACH_METADATA,
    "agent_tools.receipts.upload": _AGENT_TOOLS_RECEIPTS_UPLOAD_METADATA,
    "agent_tools.reimbursements.approve": _AGENT_TOOLS_REIMBURSEMENTS_APPROVE_METADATA,
    "agent_tools.reimbursements.cancel": _AGENT_TOOLS_REIMBURSEMENTS_CANCEL_METADATA,
    "agent_tools.reimbursements.create": _AGENT_TOOLS_REIMBURSEMENTS_CREATE_METADATA,
    "agent_tools.reimbursements.delete": _AGENT_TOOLS_REIMBURSEMENTS_DELETE_METADATA,
    "agent_tools.reimbursements.duplicate": _AGENT_TOOLS_REIMBURSEMENTS_DUPLICATE_METADATA,
    "agent_tools.reimbursements.edit": _AGENT_TOOLS_REIMBURSEMENTS_EDIT_METADATA,
    "agent_tools.reimbursements.estimate": _AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_METADATA,
    "agent_tools.reimbursements.estimate_per_diem_amount": _AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_PER_DIEM_AMOUNT_METADATA,
    "agent_tools.reimbursements.list": _AGENT_TOOLS_REIMBURSEMENTS_LIST_METADATA,
    "agent_tools.reimbursements.outstanding": _AGENT_TOOLS_REIMBURSEMENTS_OUTSTANDING_METADATA,
    "agent_tools.reimbursements.pending": _AGENT_TOOLS_REIMBURSEMENTS_PENDING_METADATA,
    "agent_tools.reimbursements.receipts": _AGENT_TOOLS_REIMBURSEMENTS_RECEIPTS_METADATA,
    "agent_tools.reimbursements.recent": _AGENT_TOOLS_REIMBURSEMENTS_RECENT_METADATA,
    "agent_tools.reimbursements.resubmit": _AGENT_TOOLS_REIMBURSEMENTS_RESUBMIT_METADATA,
    "agent_tools.reimbursements.search": _AGENT_TOOLS_REIMBURSEMENTS_SEARCH_METADATA,
    "agent_tools.reimbursements.search_reimbursements": _AGENT_TOOLS_REIMBURSEMENTS_SEARCH_REIMBURSEMENTS_METADATA,
    "agent_tools.reimbursements.submit": _AGENT_TOOLS_REIMBURSEMENTS_SUBMIT_METADATA,
    "agent_tools.requests.approve": _AGENT_TOOLS_REQUESTS_APPROVE_METADATA,
    "agent_tools.requests.get": _AGENT_TOOLS_REQUESTS_GET_METADATA,
    "agent_tools.requests.pending": _AGENT_TOOLS_REQUESTS_PENDING_METADATA,
    "agent_tools.requests.search": _AGENT_TOOLS_REQUESTS_SEARCH_METADATA,
    "agent_tools.research.help_center": _AGENT_TOOLS_RESEARCH_HELP_CENTER_METADATA,
    "agent_tools.sourcing.award": _AGENT_TOOLS_SOURCING_AWARD_METADATA,
    "agent_tools.sourcing.close_event": _AGENT_TOOLS_SOURCING_CLOSE_EVENT_METADATA,
    "agent_tools.sourcing.collaborators": _AGENT_TOOLS_SOURCING_COLLABORATORS_METADATA,
    "agent_tools.sourcing.cover_sheet": _AGENT_TOOLS_SOURCING_COVER_SHEET_METADATA,
    "agent_tools.sourcing.create": _AGENT_TOOLS_SOURCING_CREATE_METADATA,
    "agent_tools.sourcing.draft_spend_request": _AGENT_TOOLS_SOURCING_DRAFT_SPEND_REQUEST_METADATA,
    "agent_tools.sourcing.edit": _AGENT_TOOLS_SOURCING_EDIT_METADATA,
    "agent_tools.sourcing.event": _AGENT_TOOLS_SOURCING_EVENT_METADATA,
    "agent_tools.sourcing.grading": _AGENT_TOOLS_SOURCING_GRADING_METADATA,
    "agent_tools.sourcing.invitation_contact": _AGENT_TOOLS_SOURCING_INVITATION_CONTACT_METADATA,
    "agent_tools.sourcing.invite": _AGENT_TOOLS_SOURCING_INVITE_METADATA,
    "agent_tools.sourcing.list": _AGENT_TOOLS_SOURCING_LIST_METADATA,
    "agent_tools.sourcing.mark_graded": _AGENT_TOOLS_SOURCING_MARK_GRADED_METADATA,
    "agent_tools.sourcing.pricing_sheet": _AGENT_TOOLS_SOURCING_PRICING_SHEET_METADATA,
    "agent_tools.sourcing.publish": _AGENT_TOOLS_SOURCING_PUBLISH_METADATA,
    "agent_tools.sourcing.remind": _AGENT_TOOLS_SOURCING_REMIND_METADATA,
    "agent_tools.sourcing.responses": _AGENT_TOOLS_SOURCING_RESPONSES_METADATA,
    "agent_tools.sourcing.return_to_draft": _AGENT_TOOLS_SOURCING_RETURN_TO_DRAFT_METADATA,
    "agent_tools.sourcing.revoke": _AGENT_TOOLS_SOURCING_REVOKE_METADATA,
    "agent_tools.sourcing.rfx": _AGENT_TOOLS_SOURCING_RFX_METADATA,
    "agent_tools.sourcing.summary": _AGENT_TOOLS_SOURCING_SUMMARY_METADATA,
    "agent_tools.statements.outstanding": _AGENT_TOOLS_STATEMENTS_OUTSTANDING_METADATA,
    "agent_tools.tasks.list": _AGENT_TOOLS_TASKS_LIST_METADATA,
    "agent_tools.transactions.approve": _AGENT_TOOLS_TRANSACTIONS_APPROVE_METADATA,
    "agent_tools.transactions.complete_revision": _AGENT_TOOLS_TRANSACTIONS_COMPLETE_REVISION_METADATA,
    "agent_tools.transactions.edit": _AGENT_TOOLS_TRANSACTIONS_EDIT_METADATA,
    "agent_tools.transactions.explain_missing": _AGENT_TOOLS_TRANSACTIONS_EXPLAIN_MISSING_METADATA,
    "agent_tools.transactions.flag_missing": _AGENT_TOOLS_TRANSACTIONS_FLAG_MISSING_METADATA,
    "agent_tools.transactions.get": _AGENT_TOOLS_TRANSACTIONS_GET_METADATA,
    "agent_tools.transactions.list": _AGENT_TOOLS_TRANSACTIONS_LIST_METADATA,
    "agent_tools.transactions.memo_suggestions": _AGENT_TOOLS_TRANSACTIONS_MEMO_SUGGESTIONS_METADATA,
    "agent_tools.transactions.missing": _AGENT_TOOLS_TRANSACTIONS_MISSING_METADATA,
    "agent_tools.transactions.missing_by_user": _AGENT_TOOLS_TRANSACTIONS_MISSING_BY_USER_METADATA,
    "agent_tools.transactions.request_repayment": _AGENT_TOOLS_TRANSACTIONS_REQUEST_REPAYMENT_METADATA,
    "agent_tools.transactions.search_suggested_users": _AGENT_TOOLS_TRANSACTIONS_SEARCH_SUGGESTED_USERS_METADATA,
    "agent_tools.transactions.trips": _AGENT_TOOLS_TRANSACTIONS_TRIPS_METADATA,
    "agent_tools.travel.add_traveler_loyalty_program": _AGENT_TOOLS_TRAVEL_ADD_TRAVELER_LOYALTY_PROGRAM_METADATA,
    "agent_tools.travel.approve": _AGENT_TOOLS_TRAVEL_APPROVE_METADATA,
    "agent_tools.travel.book_flight": _AGENT_TOOLS_TRAVEL_BOOK_FLIGHT_METADATA,
    "agent_tools.travel.book_hotel": _AGENT_TOOLS_TRAVEL_BOOK_HOTEL_METADATA,
    "agent_tools.travel.booking_details": _AGENT_TOOLS_TRAVEL_BOOKING_DETAILS_METADATA,
    "agent_tools.travel.bookings": _AGENT_TOOLS_TRAVEL_BOOKINGS_METADATA,
    "agent_tools.travel.cancel_flight": _AGENT_TOOLS_TRAVEL_CANCEL_FLIGHT_METADATA,
    "agent_tools.travel.cancel_hotel": _AGENT_TOOLS_TRAVEL_CANCEL_HOTEL_METADATA,
    "agent_tools.travel.create": _AGENT_TOOLS_TRAVEL_CREATE_METADATA,
    "agent_tools.travel.hotel_rates": _AGENT_TOOLS_TRAVEL_HOTEL_RATES_METADATA,
    "agent_tools.travel.list": _AGENT_TOOLS_TRAVEL_LIST_METADATA,
    "agent_tools.travel.locations": _AGENT_TOOLS_TRAVEL_LOCATIONS_METADATA,
    "agent_tools.travel.loyalty_program_remove": _AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_REMOVE_METADATA,
    "agent_tools.travel.loyalty_program_set": _AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_SET_METADATA,
    "agent_tools.travel.loyalty_programs": _AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAMS_METADATA,
    "agent_tools.travel.offices": _AGENT_TOOLS_TRAVEL_OFFICES_METADATA,
    "agent_tools.travel.pending": _AGENT_TOOLS_TRAVEL_PENDING_METADATA,
    "agent_tools.travel.profile": _AGENT_TOOLS_TRAVEL_PROFILE_METADATA,
    "agent_tools.travel.profile_update": _AGENT_TOOLS_TRAVEL_PROFILE_UPDATE_METADATA,
    "agent_tools.travel.search_flight": _AGENT_TOOLS_TRAVEL_SEARCH_FLIGHT_METADATA,
    "agent_tools.travel.search_hotel": _AGENT_TOOLS_TRAVEL_SEARCH_HOTEL_METADATA,
    "agent_tools.travel.update_traveler_loyalty_program": _AGENT_TOOLS_TRAVEL_UPDATE_TRAVELER_LOYALTY_PROGRAM_METADATA,
    "agent_tools.treasury.accounts": _AGENT_TOOLS_TREASURY_ACCOUNTS_METADATA,
    "agent_tools.treasury.balance_history": _AGENT_TOOLS_TREASURY_BALANCE_HISTORY_METADATA,
    "agent_tools.treasury.history": _AGENT_TOOLS_TREASURY_HISTORY_METADATA,
    "agent_tools.treasury.investments": _AGENT_TOOLS_TREASURY_INVESTMENTS_METADATA,
    "agent_tools.treasury.list": _AGENT_TOOLS_TREASURY_LIST_METADATA,
    "agent_tools.treasury.portfolio": _AGENT_TOOLS_TREASURY_PORTFOLIO_METADATA,
    "agent_tools.treasury.summary": _AGENT_TOOLS_TREASURY_SUMMARY_METADATA,
    "agent_tools.treasury.transfers": _AGENT_TOOLS_TREASURY_TRANSFERS_METADATA,
    "agent_tools.users.list": _AGENT_TOOLS_USERS_LIST_METADATA,
    "agent_tools.users.me": _AGENT_TOOLS_USERS_ME_METADATA,
    "agent_tools.users.org_chart": _AGENT_TOOLS_USERS_ORG_CHART_METADATA,
    "agent_tools.vendors.attach_document": _AGENT_TOOLS_VENDORS_ATTACH_DOCUMENT_METADATA,
    "agent_tools.vendors.bulk_upload": _AGENT_TOOLS_VENDORS_BULK_UPLOAD_METADATA,
    "agent_tools.vendors.bulk_upload_status": _AGENT_TOOLS_VENDORS_BULK_UPLOAD_STATUS_METADATA,
    "agent_tools.vendors.create": _AGENT_TOOLS_VENDORS_CREATE_METADATA,
    "agent_tools.vendors.get": _AGENT_TOOLS_VENDORS_GET_METADATA,
    "agent_tools.vendors.list": _AGENT_TOOLS_VENDORS_LIST_METADATA,
    "agent_tools.vendors.search": _AGENT_TOOLS_VENDORS_SEARCH_METADATA,
    "agent_tools.x402.create": _AGENT_TOOLS_X402_CREATE_METADATA,
    "agent_tools.x402.fund": _AGENT_TOOLS_X402_FUND_METADATA,
    "agent_tools.x402.pay": _AGENT_TOOLS_X402_PAY_METADATA,
    "agent_tools.x402.withdraw": _AGENT_TOOLS_X402_WITHDRAW_METADATA,
    "accounting.mark_ready_to_sync": _DEVELOPER_API_ACCOUNTING_MARK_READY_TO_SYNC_METADATA,
    "agent_wallet.list": _DEVELOPER_API_AGENT_WALLET_LIST_METADATA,
    "agent_wallet.publish_policy": _DEVELOPER_API_AGENT_WALLET_PUBLISH_POLICY_METADATA,
    "agents.create": _DEVELOPER_API_AGENTS_CREATE_METADATA,
    "agents.delete": _DEVELOPER_API_AGENTS_DELETE_METADATA,
    "agents.get": _DEVELOPER_API_AGENTS_GET_METADATA,
    "agents.list": _DEVELOPER_API_AGENTS_LIST_METADATA,
    "agents.rotate_secret": _DEVELOPER_API_AGENTS_ROTATE_SECRET_METADATA,
    "agents.set_status": _DEVELOPER_API_AGENTS_SET_STATUS_METADATA,
    "agents.update": _DEVELOPER_API_AGENTS_UPDATE_METADATA,
    "applications.delete_document": _DEVELOPER_API_APPLICATIONS_DELETE_DOCUMENT_METADATA,
    "applications.documents": _DEVELOPER_API_APPLICATIONS_DOCUMENTS_METADATA,
    "applications.edit": _DEVELOPER_API_APPLICATIONS_EDIT_METADATA,
    "applications.followups": _DEVELOPER_API_APPLICATIONS_FOLLOWUPS_METADATA,
    "applications.get": _DEVELOPER_API_APPLICATIONS_GET_METADATA,
    "applications.progress": _DEVELOPER_API_APPLICATIONS_PROGRESS_METADATA,
    "applications.submit": _DEVELOPER_API_APPLICATIONS_SUBMIT_METADATA,
    "applications.update_followup": _DEVELOPER_API_APPLICATIONS_UPDATE_FOLLOWUP_METADATA,
    "applications.upload": _DEVELOPER_API_APPLICATIONS_UPLOAD_METADATA,
    "ask_ramp.ask": _DEVELOPER_API_ASK_RAMP_ASK_METADATA,
    "ask_ramp.continue_": _DEVELOPER_API_ASK_RAMP_CONTINUE__METADATA,
    "ask_ramp.get_result": _DEVELOPER_API_ASK_RAMP_GET_RESULT_METADATA,
    "bank_link.accounts": _DEVELOPER_API_BANK_LINK_ACCOUNTS_METADATA,
    "bank_link.create": _DEVELOPER_API_BANK_LINK_CREATE_METADATA,
    "merchant.list": _DEVELOPER_API_MERCHANT_LIST_METADATA,
    "sourcing.upload": _DEVELOPER_API_SOURCING_UPLOAD_METADATA,
    "statements.get": _DEVELOPER_API_STATEMENTS_GET_METADATA,
    "statements.list": _DEVELOPER_API_STATEMENTS_LIST_METADATA,
    "transactions.split": _DEVELOPER_API_TRANSACTIONS_SPLIT_METADATA,
    "treasury.account_numbers": _DEVELOPER_API_TREASURY_ACCOUNT_NUMBERS_METADATA,
    "treasury.request_funds": _DEVELOPER_API_TREASURY_REQUEST_FUNDS_METADATA,
    "users.roles": _DEVELOPER_API_USERS_ROLES_METADATA,
}


def _without_not_given(values: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value for key, value in values.items() if not isinstance(value, NotGiven)
    }


class AgentToolsAccounting:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def categories(
        self,
        *,
        include_hidden: bool | NotGiven = NOT_GIVEN,
        rationale: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTrackingCategoriesResult:
        """Retrieve active accounting tracking category metadata for transaction coding, such (post_agent_tool_api___get_tracking_categories)."""
        return cast(
            GetTrackingCategoriesResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-tracking-categories",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_hidden": include_hidden,
                        "rationale": rationale,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_CATEGORIES_METADATA,
            ),
        )

    def category_options(
        self,
        *,
        include_hidden: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: int | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        query_string: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        tracking_category_uuid: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTrackingCategoryOptionsResult:
        """List specific departments, projects, or other options for a tracking category (post_agent_tool_api___get_tracking_category_options)."""
        return cast(
            GetTrackingCategoryOptionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-tracking-category-options",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_hidden": include_hidden,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "query_string": query_string,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "tracking_category_uuid": tracking_category_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_CATEGORY_OPTIONS_METADATA,
            ),
        )

    def latest_sync(
        self,
        *,
        rationale: str,
        sync_type: str,
    ) -> GetLatestSyncResponse:
        """Get the most recent accounting sync commit for the acting user's business and sync type (post_agent_tool_api___get_latest_sync)."""
        return cast(
            GetLatestSyncResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-latest-sync",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sync_type": sync_type}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_LATEST_SYNC_METADATA,
            ),
        )

    def sync_failures(
        self,
        *,
        rationale: str,
        sync_commit_uuid: str,
    ) -> GetSyncCommitFailureDetailsResult:
        """Get object-level failure details for an accounting sync commit by UUID (post_agent_tool_api___get_sync_commit_failure_details)."""
        return cast(
            GetSyncCommitFailureDetailsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-sync-commit-failure-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sync_commit_uuid": sync_commit_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_SYNC_FAILURES_METADATA,
            ),
        )


class AsyncAgentToolsAccounting:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def categories(
        self,
        *,
        include_hidden: bool | NotGiven = NOT_GIVEN,
        rationale: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTrackingCategoriesResult:
        """Retrieve active accounting tracking category metadata for transaction coding, such (post_agent_tool_api___get_tracking_categories)."""
        return cast(
            GetTrackingCategoriesResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-tracking-categories",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_hidden": include_hidden,
                        "rationale": rationale,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_CATEGORIES_METADATA,
            ),
        )

    async def category_options(
        self,
        *,
        include_hidden: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: int | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        query_string: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        tracking_category_uuid: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTrackingCategoryOptionsResult:
        """List specific departments, projects, or other options for a tracking category (post_agent_tool_api___get_tracking_category_options)."""
        return cast(
            GetTrackingCategoryOptionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-tracking-category-options",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_hidden": include_hidden,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "query_string": query_string,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "tracking_category_uuid": tracking_category_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_CATEGORY_OPTIONS_METADATA,
            ),
        )

    async def latest_sync(
        self,
        *,
        rationale: str,
        sync_type: str,
    ) -> GetLatestSyncResponse:
        """Get the most recent accounting sync commit for the acting user's business and sync type (post_agent_tool_api___get_latest_sync)."""
        return cast(
            GetLatestSyncResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-latest-sync",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sync_type": sync_type}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_LATEST_SYNC_METADATA,
            ),
        )

    async def sync_failures(
        self,
        *,
        rationale: str,
        sync_commit_uuid: str,
    ) -> GetSyncCommitFailureDetailsResult:
        """Get object-level failure details for an accounting sync commit by UUID (post_agent_tool_api___get_sync_commit_failure_details)."""
        return cast(
            GetSyncCommitFailureDetailsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-sync-commit-failure-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sync_commit_uuid": sync_commit_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ACCOUNTING_SYNC_FAILURES_METADATA,
            ),
        )


class AgentToolsAgentCards:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create_payment_token(
        self,
        *,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        amount: str,
        currency_code: str,
        fund_id: str,
        merchant_country_code: str,
        merchant_name: str,
        merchant_url: str,
        rationale: str,
    ) -> PaymentTokenResult:
        """Get a one-time payment token for a fund (post_agent_tool_api___get_agent_card_creds)."""
        return cast(
            PaymentTokenResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-agent-card-creds",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency_code": currency_code,
                        "fund_id": fund_id,
                        "merchant_country_code": merchant_country_code,
                        "merchant_name": merchant_name,
                        "merchant_url": merchant_url,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_CREATE_PAYMENT_TOKEN_METADATA,
            ),
        )

    def enroll(
        self,
        *,
        rationale: str,
    ) -> ToolStringOutput:
        """Enroll the current business in agent cards for agentic commerce (post_agent_tool_api___enroll_business_in_agent_cards)."""
        return cast(
            ToolStringOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/enroll-business-in-agent-cards",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_ENROLL_METADATA,
            ),
        )

    def list_funds(
        self,
        *,
        rationale: str,
    ) -> AgentCardFundsList:
        """List funds that can be used for agent card payments (post_agent_tool_api___get_agent_card_funds)."""
        return cast(
            AgentCardFundsList,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-agent-card-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_LIST_FUNDS_METADATA,
            ),
        )


class AsyncAgentToolsAgentCards:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create_payment_token(
        self,
        *,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        amount: str,
        currency_code: str,
        fund_id: str,
        merchant_country_code: str,
        merchant_name: str,
        merchant_url: str,
        rationale: str,
    ) -> PaymentTokenResult:
        """Get a one-time payment token for a fund (post_agent_tool_api___get_agent_card_creds)."""
        return cast(
            PaymentTokenResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-agent-card-creds",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency_code": currency_code,
                        "fund_id": fund_id,
                        "merchant_country_code": merchant_country_code,
                        "merchant_name": merchant_name,
                        "merchant_url": merchant_url,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_CREATE_PAYMENT_TOKEN_METADATA,
            ),
        )

    async def enroll(
        self,
        *,
        rationale: str,
    ) -> ToolStringOutput:
        """Enroll the current business in agent cards for agentic commerce (post_agent_tool_api___enroll_business_in_agent_cards)."""
        return cast(
            ToolStringOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/enroll-business-in-agent-cards",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_ENROLL_METADATA,
            ),
        )

    async def list_funds(
        self,
        *,
        rationale: str,
    ) -> AgentCardFundsList:
        """List funds that can be used for agent card payments (post_agent_tool_api___get_agent_card_funds)."""
        return cast(
            AgentCardFundsList,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-agent-card-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AGENT_CARDS_LIST_FUNDS_METADATA,
            ),
        )


class AgentToolsAiTokenSpend:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def aggregates(
        self,
        *,
        configuration_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        department_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        end_at: str,
        group_by: Sequence[str] | NotGiven = NOT_GIVEN,
        metric: str,
        model_compute_tier: Sequence[str] | NotGiven = NOT_GIVEN,
        model_context_window: Sequence[str] | NotGiven = NOT_GIVEN,
        model_families: Sequence[str] | NotGiven = NOT_GIVEN,
        model_fine_tune_source: Sequence[str] | NotGiven = NOT_GIVEN,
        model_speed: Sequence[str] | NotGiven = NOT_GIVEN,
        model_thinking: Sequence[str] | NotGiven = NOT_GIVEN,
        models: Sequence[str] | NotGiven = NOT_GIVEN,
        providers: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
        rollup: str | NotGiven = NOT_GIVEN,
        start_at: str,
        tag_definition_id: str | None | NotGiven = NOT_GIVEN,
        user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> AiTokenSpendAggregatesResult:
        """Aggregate AI token usage or estimated cost over a time window, grouped by caller-selected dimensions (provider, model, configuration, department, user, or API-key tag group) (post_agent_tool_api___get_ai_token_spend_aggregates)."""
        return cast(
            AiTokenSpendAggregatesResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-aggregates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "configuration_ids": configuration_ids,
                        "department_uuids": department_uuids,
                        "end_at": end_at,
                        "group_by": group_by,
                        "metric": metric,
                        "model_compute_tier": model_compute_tier,
                        "model_context_window": model_context_window,
                        "model_families": model_families,
                        "model_fine_tune_source": model_fine_tune_source,
                        "model_speed": model_speed,
                        "model_thinking": model_thinking,
                        "models": models,
                        "providers": providers,
                        "rationale": rationale,
                        "rollup": rollup,
                        "start_at": start_at,
                        "tag_definition_id": tag_definition_id,
                        "user_uuids": user_uuids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_AGGREGATES_METADATA,
            ),
        )

    def connections(
        self,
        *,
        rationale: str,
    ) -> AiTokenSpendConnectionsResult:
        """Summarize connected AI providers (admin keys and OpenRouter/LiteLLM gateway connections) (post_agent_tool_api___get_ai_token_spend_connections)."""
        return cast(
            AiTokenSpendConnectionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-connections",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_CONNECTIONS_METADATA,
            ),
        )

    def current_spend(
        self,
        *,
        rationale: str,
    ) -> AiCurrentSpendResponseSchema:
        """Report the business's actual trailing-30-day Ramp spend on AI vendors (card, bill, and reimbursement spend) per provider (post_agent_tool_api___get_ai_token_spend_current_spend)."""
        return cast(
            AiCurrentSpendResponseSchema,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-current-spend",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_CURRENT_SPEND_METADATA,
            ),
        )

    def filter_options(
        self,
        *,
        rationale: str,
    ) -> AiTokenSpendFilterOptionsResult:
        """List the dimensions and values available for AI-spend aggregate queries: providers, models, model families/facets, departments, and API-key tag groups (post_agent_tool_api___get_ai_token_spend_filter_options)."""
        return cast(
            AiTokenSpendFilterOptionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-filter-options",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_FILTER_OPTIONS_METADATA,
            ),
        )

    def me(
        self,
        *,
        end_at: str,
        group_by: Sequence[str] | NotGiven = NOT_GIVEN,
        model_compute_tier: Sequence[str] | NotGiven = NOT_GIVEN,
        model_context_window: Sequence[str] | NotGiven = NOT_GIVEN,
        model_families: Sequence[str] | NotGiven = NOT_GIVEN,
        model_fine_tune_source: Sequence[str] | NotGiven = NOT_GIVEN,
        model_speed: Sequence[str] | NotGiven = NOT_GIVEN,
        model_thinking: Sequence[str] | NotGiven = NOT_GIVEN,
        models: Sequence[str] | NotGiven = NOT_GIVEN,
        providers: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
        rollup: str | NotGiven = NOT_GIVEN,
        start_at: str,
    ) -> AggregatedUsageResponseSchema:
        """Aggregate the acting user's own AI token usage and estimated token cost over a time window, optionally grouped by provider and model (post_agent_tool_api___get_my_ai_token_spend_aggregates)."""
        return cast(
            AggregatedUsageResponseSchema,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-my-ai-token-spend-aggregates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "end_at": end_at,
                        "group_by": group_by,
                        "model_compute_tier": model_compute_tier,
                        "model_context_window": model_context_window,
                        "model_families": model_families,
                        "model_fine_tune_source": model_fine_tune_source,
                        "model_speed": model_speed,
                        "model_thinking": model_thinking,
                        "models": models,
                        "providers": providers,
                        "rationale": rationale,
                        "rollup": rollup,
                        "start_at": start_at,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_ME_METADATA,
            ),
        )


class AsyncAgentToolsAiTokenSpend:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def aggregates(
        self,
        *,
        configuration_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        department_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        end_at: str,
        group_by: Sequence[str] | NotGiven = NOT_GIVEN,
        metric: str,
        model_compute_tier: Sequence[str] | NotGiven = NOT_GIVEN,
        model_context_window: Sequence[str] | NotGiven = NOT_GIVEN,
        model_families: Sequence[str] | NotGiven = NOT_GIVEN,
        model_fine_tune_source: Sequence[str] | NotGiven = NOT_GIVEN,
        model_speed: Sequence[str] | NotGiven = NOT_GIVEN,
        model_thinking: Sequence[str] | NotGiven = NOT_GIVEN,
        models: Sequence[str] | NotGiven = NOT_GIVEN,
        providers: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
        rollup: str | NotGiven = NOT_GIVEN,
        start_at: str,
        tag_definition_id: str | None | NotGiven = NOT_GIVEN,
        user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> AiTokenSpendAggregatesResult:
        """Aggregate AI token usage or estimated cost over a time window, grouped by caller-selected dimensions (provider, model, configuration, department, user, or API-key tag group) (post_agent_tool_api___get_ai_token_spend_aggregates)."""
        return cast(
            AiTokenSpendAggregatesResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-aggregates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "configuration_ids": configuration_ids,
                        "department_uuids": department_uuids,
                        "end_at": end_at,
                        "group_by": group_by,
                        "metric": metric,
                        "model_compute_tier": model_compute_tier,
                        "model_context_window": model_context_window,
                        "model_families": model_families,
                        "model_fine_tune_source": model_fine_tune_source,
                        "model_speed": model_speed,
                        "model_thinking": model_thinking,
                        "models": models,
                        "providers": providers,
                        "rationale": rationale,
                        "rollup": rollup,
                        "start_at": start_at,
                        "tag_definition_id": tag_definition_id,
                        "user_uuids": user_uuids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_AGGREGATES_METADATA,
            ),
        )

    async def connections(
        self,
        *,
        rationale: str,
    ) -> AiTokenSpendConnectionsResult:
        """Summarize connected AI providers (admin keys and OpenRouter/LiteLLM gateway connections) (post_agent_tool_api___get_ai_token_spend_connections)."""
        return cast(
            AiTokenSpendConnectionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-connections",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_CONNECTIONS_METADATA,
            ),
        )

    async def current_spend(
        self,
        *,
        rationale: str,
    ) -> AiCurrentSpendResponseSchema:
        """Report the business's actual trailing-30-day Ramp spend on AI vendors (card, bill, and reimbursement spend) per provider (post_agent_tool_api___get_ai_token_spend_current_spend)."""
        return cast(
            AiCurrentSpendResponseSchema,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-current-spend",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_CURRENT_SPEND_METADATA,
            ),
        )

    async def filter_options(
        self,
        *,
        rationale: str,
    ) -> AiTokenSpendFilterOptionsResult:
        """List the dimensions and values available for AI-spend aggregate queries: providers, models, model families/facets, departments, and API-key tag groups (post_agent_tool_api___get_ai_token_spend_filter_options)."""
        return cast(
            AiTokenSpendFilterOptionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-ai-token-spend-filter-options",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_FILTER_OPTIONS_METADATA,
            ),
        )

    async def me(
        self,
        *,
        end_at: str,
        group_by: Sequence[str] | NotGiven = NOT_GIVEN,
        model_compute_tier: Sequence[str] | NotGiven = NOT_GIVEN,
        model_context_window: Sequence[str] | NotGiven = NOT_GIVEN,
        model_families: Sequence[str] | NotGiven = NOT_GIVEN,
        model_fine_tune_source: Sequence[str] | NotGiven = NOT_GIVEN,
        model_speed: Sequence[str] | NotGiven = NOT_GIVEN,
        model_thinking: Sequence[str] | NotGiven = NOT_GIVEN,
        models: Sequence[str] | NotGiven = NOT_GIVEN,
        providers: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
        rollup: str | NotGiven = NOT_GIVEN,
        start_at: str,
    ) -> AggregatedUsageResponseSchema:
        """Aggregate the acting user's own AI token usage and estimated token cost over a time window, optionally grouped by provider and model (post_agent_tool_api___get_my_ai_token_spend_aggregates)."""
        return cast(
            AggregatedUsageResponseSchema,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-my-ai-token-spend-aggregates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "end_at": end_at,
                        "group_by": group_by,
                        "model_compute_tier": model_compute_tier,
                        "model_context_window": model_context_window,
                        "model_families": model_families,
                        "model_fine_tune_source": model_fine_tune_source,
                        "model_speed": model_speed,
                        "model_thinking": model_thinking,
                        "models": models,
                        "providers": providers,
                        "rationale": rationale,
                        "rollup": rollup,
                        "start_at": start_at,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_AI_TOKEN_SPEND_ME_METADATA,
            ),
        )


class AgentToolsAnalyst:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def catalog(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystCatalogResponse:
        """Discover available analyst tables and starter SQL for aggregate business analysis (post_agent_tool_api___get_analyst_catalog)."""
        return cast(
            PublicAnalystCatalogResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-catalog",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_CATALOG_METADATA,
            ),
        )

    def metrics(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystMetricMetadataResponse:
        """Discover supported analyst metrics and starter SQL for aggregate business analysis (post_agent_tool_api___get_analyst_metric_metadata)."""
        return cast(
            PublicAnalystMetricMetadataResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-metric-metadata",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_METRICS_METADATA,
            ),
        )

    def query(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
        sql: str,
    ) -> PublicAnalystQueryResponse:
        """Run read-only SQL for aggregate business analysis (post_agent_tool_api___execute_analyst_query)."""
        return cast(
            PublicAnalystQueryResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/execute-analyst-query",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                        "sql": sql,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_QUERY_METADATA,
            ),
        )

    def spend_docs(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystTableDomainDocsResponse:
        """Read domain documentation for analyst.spend_facts before using it in an analyst query (post_agent_tool_api___get_analyst_spend_facts_domain_docs)."""
        return cast(
            PublicAnalystTableDomainDocsResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-spend-facts-domain-docs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_SPEND_DOCS_METADATA,
            ),
        )

    def table_docs(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        qualified_name: str,
        rationale: str,
    ) -> PublicAnalystTableDomainDocsResponse:
        """Read domain documentation for an analyst table before using it in an analyst query (post_agent_tool_api___get_analyst_table_domain_docs)."""
        return cast(
            PublicAnalystTableDomainDocsResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-table-domain-docs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "qualified_name": qualified_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_TABLE_DOCS_METADATA,
            ),
        )


class AsyncAgentToolsAnalyst:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def catalog(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystCatalogResponse:
        """Discover available analyst tables and starter SQL for aggregate business analysis (post_agent_tool_api___get_analyst_catalog)."""
        return cast(
            PublicAnalystCatalogResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-catalog",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_CATALOG_METADATA,
            ),
        )

    async def metrics(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystMetricMetadataResponse:
        """Discover supported analyst metrics and starter SQL for aggregate business analysis (post_agent_tool_api___get_analyst_metric_metadata)."""
        return cast(
            PublicAnalystMetricMetadataResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-metric-metadata",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_METRICS_METADATA,
            ),
        )

    async def query(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
        sql: str,
    ) -> PublicAnalystQueryResponse:
        """Run read-only SQL for aggregate business analysis (post_agent_tool_api___execute_analyst_query)."""
        return cast(
            PublicAnalystQueryResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/execute-analyst-query",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                        "sql": sql,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_QUERY_METADATA,
            ),
        )

    async def spend_docs(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PublicAnalystTableDomainDocsResponse:
        """Read domain documentation for analyst.spend_facts before using it in an analyst query (post_agent_tool_api___get_analyst_spend_facts_domain_docs)."""
        return cast(
            PublicAnalystTableDomainDocsResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-spend-facts-domain-docs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_SPEND_DOCS_METADATA,
            ),
        )

    async def table_docs(
        self,
        *,
        artifact_instance_id: str | NotGiven = NOT_GIVEN,
        qualified_name: str,
        rationale: str,
    ) -> PublicAnalystTableDomainDocsResponse:
        """Read domain documentation for an analyst table before using it in an analyst query (post_agent_tool_api___get_analyst_table_domain_docs)."""
        return cast(
            PublicAnalystTableDomainDocsResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-analyst-table-domain-docs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "artifact_instance_id": artifact_instance_id,
                        "qualified_name": qualified_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_ANALYST_TABLE_DOCS_METADATA,
            ),
        )


class AgentToolsBills:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def amount_summary(
        self,
        *,
        due_date_from: str | None | NotGiven = NOT_GIVEN,
        due_date_to: str | None | NotGiven = NOT_GIVEN,
        max_amount: float | None | NotGiven = NOT_GIVEN,
        min_amount: float | None | NotGiven = NOT_GIVEN,
        payment_status: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> GetBillAmountSummaryResult:
        """Get aggregate dollar amounts for bills matching the given filters (post_agent_tool_api___get_bill_amount_summary)."""
        return cast(
            GetBillAmountSummaryResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-amount-summary",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "due_date_from": due_date_from,
                        "due_date_to": due_date_to,
                        "max_amount": max_amount,
                        "min_amount": min_amount,
                        "payment_status": payment_status,
                        "rationale": rationale,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_AMOUNT_SUMMARY_METADATA,
            ),
        )

    def approve(
        self,
        *,
        action_type: str,
        bill_id: str,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
    ) -> BillActionResult:
        """Approve or reject a submitted bill that is pending approval (post_agent_tool_api___approve_or_reject_bill)."""
        return cast(
            BillActionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action_type": action_type,
                        "bill_id": bill_id,
                        "rationale": rationale,
                        "reason": reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_APPROVE_METADATA,
            ),
        )

    def attachments(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillInvoicesResult:
        """Retrieve invoice file attachments (PDFs/images) for a submitted bill (post_agent_tool_api___get_bill_invoices)."""
        return cast(
            BillInvoicesResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-invoices",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_ATTACHMENTS_METADATA,
            ),
        )

    def comments(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillCommentsResult:
        """Retrieve comments from a bill's comment thread (post_agent_tool_api___get_bill_comments)."""
        return cast(
            BillCommentsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-comments",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_COMMENTS_METADATA,
            ),
        )

    def create(
        self,
        *,
        idempotency_key: str,
        draft_bill: dict[str, Any],
        rationale: str,
        vendor_uuid: UUID,
    ) -> CreateDraftBillResult:
        """Create a new draft bill for an existing vendor (post_agent_tool_api___create_draft_bill)."""
        return cast(
            CreateDraftBillResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-draft-bill",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "draft_bill": draft_bill,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_CREATE_METADATA,
            ),
        )

    def draft(
        self,
        *,
        bill_id: str,
        rationale: str,
        return_line_items: bool | NotGiven = NOT_GIVEN,
    ) -> DraftBillDetails:
        """Get rich details for a draft bill (post_agent_tool_api___get_draft_bill_details)."""
        return cast(
            DraftBillDetails,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-draft-bill-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "bill_id": bill_id,
                        "rationale": rationale,
                        "return_line_items": return_line_items,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_DRAFT_METADATA,
            ),
        )

    def edit(
        self,
        *,
        provisional_bill: dict[str, Any],
        provisional_bill_id: str,
        rationale: str,
        vendor_payments: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        version: str,
    ) -> PatchProvisionalBillResult:
        """Update a draft bill: its fields, line items, accounting category coding, and draft payment details (post_agent_tool_api___patch_provisional_bill)."""
        return cast(
            PatchProvisionalBillResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-draft-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "provisional_bill": provisional_bill,
                        "provisional_bill_id": provisional_bill_id,
                        "rationale": rationale,
                        "vendor_payments": vendor_payments,
                        "version": version,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_EDIT_METADATA,
            ),
        )

    def get(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillDetails:
        """Get comprehensive details about a specific bill including payment status, approval status, and all metadata (post_agent_tool_api___get_bill_details)."""
        return cast(
            BillDetails,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_GET_METADATA,
            ),
        )

    def history(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillHistoryResult:
        """Retrieve the full modification and approval history of a bill, including status changes, approval actions, and creation details (post_agent_tool_api___get_bill_history)."""
        return cast(
            BillHistoryResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-history",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_HISTORY_METADATA,
            ),
        )

    def list(
        self,
        *,
        include_paid: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        query: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> BillSearchResult:
        """List and filter bills with optional search, pagination, and status filters (post_agent_tool_api___list_bills)."""
        return cast(
            BillSearchResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-bills",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_paid": include_paid,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "query": query,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_LIST_METADATA,
            ),
        )

    def metrics(
        self,
        *,
        approval_status: str | None | NotGiven = NOT_GIVEN,
        from_due_date: str | None | NotGiven = NOT_GIVEN,
        is_draft: bool | None | NotGiven = NOT_GIVEN,
        payment_status: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        status_summary: str | None | NotGiven = NOT_GIVEN,
        to_due_date: str | None | NotGiven = NOT_GIVEN,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> GetBillMetricsResult:
        """Returns the count of bills matching specified filters (post_agent_tool_api___get_bill_metrics)."""
        return cast(
            GetBillMetricsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-metrics",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "approval_status": approval_status,
                        "from_due_date": from_due_date,
                        "is_draft": is_draft,
                        "payment_status": payment_status,
                        "rationale": rationale,
                        "status_summary": status_summary,
                        "to_due_date": to_due_date,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_METRICS_METADATA,
            ),
        )

    def pending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> BillSearchResult:
        """Get bills that are pending approval from the current user (post_agent_tool_api___get_bills_for_approval)."""
        return cast(
            BillSearchResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bills-for-approval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"limit": limit, "page_cursor": page_cursor, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_PENDING_METADATA,
            ),
        )

    def recurring(
        self,
        *,
        rationale: str,
        recurring_bill_id: str,
    ) -> RecurringBillDetails:
        """Retrieve details of a recurring bill template including vendor, amount, recurrence schedule, and next payment date (post_agent_tool_api___get_recurring_bill)."""
        return cast(
            RecurringBillDetails,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-recurring-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "recurring_bill_id": recurring_bill_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_RECURRING_METADATA,
            ),
        )

    def remind(
        self,
        *,
        bill_uuids: Sequence[UUID],
        rationale: str,
    ) -> BillApproverReminderResult:
        """Remind next approvers for bills awaiting approval (post_agent_tool_api___remind_bill_approvers)."""
        return cast(
            BillApproverReminderResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remind-bill-approvers",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"bill_uuids": bill_uuids, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_REMIND_METADATA,
            ),
        )

    def search(
        self,
        *,
        accrual_year_month: str | None | NotGiven = NOT_GIVEN,
        from_due_date: str | None | NotGiven = NOT_GIVEN,
        from_payment_date: str | None | NotGiven = NOT_GIVEN,
        include_drafts: bool | None | NotGiven = NOT_GIVEN,
        include_paid: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        rationale: str,
        status_summaries: Sequence[str] | None | NotGiven = NOT_GIVEN,
        to_due_date: str | None | NotGiven = NOT_GIVEN,
        to_payment_date: str | None | NotGiven = NOT_GIVEN,
    ) -> BillSearchResult:
        """Search for bills using natural language queries like vendor names, amounts, or invoice numbers (post_agent_tool_api___search_bills)."""
        return cast(
            BillSearchResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-bills",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accrual_year_month": accrual_year_month,
                        "from_due_date": from_due_date,
                        "from_payment_date": from_payment_date,
                        "include_drafts": include_drafts,
                        "include_paid": include_paid,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "query": query,
                        "rationale": rationale,
                        "status_summaries": status_summaries,
                        "to_due_date": to_due_date,
                        "to_payment_date": to_payment_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_SEARCH_METADATA,
            ),
        )

    def status(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillStatus:
        """Get the current payment and approval status of a specific bill, including any required next actions (post_agent_tool_api___get_bill_status)."""
        return cast(
            BillStatus,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-status",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_STATUS_METADATA,
            ),
        )

    def submit(
        self,
        *,
        draft_bill_id: UUID,
        rationale: str,
    ) -> SubmitDraftBillResult:
        """Submit a ready draft bill for approval (post_agent_tool_api___submit_draft_bill)."""
        return cast(
            SubmitDraftBillResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-draft-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"draft_bill_id": draft_bill_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_SUBMIT_METADATA,
            ),
        )


class AsyncAgentToolsBills:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def amount_summary(
        self,
        *,
        due_date_from: str | None | NotGiven = NOT_GIVEN,
        due_date_to: str | None | NotGiven = NOT_GIVEN,
        max_amount: float | None | NotGiven = NOT_GIVEN,
        min_amount: float | None | NotGiven = NOT_GIVEN,
        payment_status: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> GetBillAmountSummaryResult:
        """Get aggregate dollar amounts for bills matching the given filters (post_agent_tool_api___get_bill_amount_summary)."""
        return cast(
            GetBillAmountSummaryResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-amount-summary",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "due_date_from": due_date_from,
                        "due_date_to": due_date_to,
                        "max_amount": max_amount,
                        "min_amount": min_amount,
                        "payment_status": payment_status,
                        "rationale": rationale,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_AMOUNT_SUMMARY_METADATA,
            ),
        )

    async def approve(
        self,
        *,
        action_type: str,
        bill_id: str,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
    ) -> BillActionResult:
        """Approve or reject a submitted bill that is pending approval (post_agent_tool_api___approve_or_reject_bill)."""
        return cast(
            BillActionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action_type": action_type,
                        "bill_id": bill_id,
                        "rationale": rationale,
                        "reason": reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_APPROVE_METADATA,
            ),
        )

    async def attachments(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillInvoicesResult:
        """Retrieve invoice file attachments (PDFs/images) for a submitted bill (post_agent_tool_api___get_bill_invoices)."""
        return cast(
            BillInvoicesResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-invoices",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_ATTACHMENTS_METADATA,
            ),
        )

    async def comments(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillCommentsResult:
        """Retrieve comments from a bill's comment thread (post_agent_tool_api___get_bill_comments)."""
        return cast(
            BillCommentsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-comments",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_COMMENTS_METADATA,
            ),
        )

    async def create(
        self,
        *,
        idempotency_key: str,
        draft_bill: dict[str, Any],
        rationale: str,
        vendor_uuid: UUID,
    ) -> CreateDraftBillResult:
        """Create a new draft bill for an existing vendor (post_agent_tool_api___create_draft_bill)."""
        return cast(
            CreateDraftBillResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-draft-bill",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "draft_bill": draft_bill,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_CREATE_METADATA,
            ),
        )

    async def draft(
        self,
        *,
        bill_id: str,
        rationale: str,
        return_line_items: bool | NotGiven = NOT_GIVEN,
    ) -> DraftBillDetails:
        """Get rich details for a draft bill (post_agent_tool_api___get_draft_bill_details)."""
        return cast(
            DraftBillDetails,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-draft-bill-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "bill_id": bill_id,
                        "rationale": rationale,
                        "return_line_items": return_line_items,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_DRAFT_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        provisional_bill: dict[str, Any],
        provisional_bill_id: str,
        rationale: str,
        vendor_payments: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        version: str,
    ) -> PatchProvisionalBillResult:
        """Update a draft bill: its fields, line items, accounting category coding, and draft payment details (post_agent_tool_api___patch_provisional_bill)."""
        return cast(
            PatchProvisionalBillResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-draft-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "provisional_bill": provisional_bill,
                        "provisional_bill_id": provisional_bill_id,
                        "rationale": rationale,
                        "vendor_payments": vendor_payments,
                        "version": version,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_EDIT_METADATA,
            ),
        )

    async def get(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillDetails:
        """Get comprehensive details about a specific bill including payment status, approval status, and all metadata (post_agent_tool_api___get_bill_details)."""
        return cast(
            BillDetails,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_GET_METADATA,
            ),
        )

    async def history(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillHistoryResult:
        """Retrieve the full modification and approval history of a bill, including status changes, approval actions, and creation details (post_agent_tool_api___get_bill_history)."""
        return cast(
            BillHistoryResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-history",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_HISTORY_METADATA,
            ),
        )

    async def list(
        self,
        *,
        include_paid: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        query: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> BillSearchResult:
        """List and filter bills with optional search, pagination, and status filters (post_agent_tool_api___list_bills)."""
        return cast(
            BillSearchResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-bills",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_paid": include_paid,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "query": query,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_LIST_METADATA,
            ),
        )

    async def metrics(
        self,
        *,
        approval_status: str | None | NotGiven = NOT_GIVEN,
        from_due_date: str | None | NotGiven = NOT_GIVEN,
        is_draft: bool | None | NotGiven = NOT_GIVEN,
        payment_status: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        status_summary: str | None | NotGiven = NOT_GIVEN,
        to_due_date: str | None | NotGiven = NOT_GIVEN,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> GetBillMetricsResult:
        """Returns the count of bills matching specified filters (post_agent_tool_api___get_bill_metrics)."""
        return cast(
            GetBillMetricsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-metrics",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "approval_status": approval_status,
                        "from_due_date": from_due_date,
                        "is_draft": is_draft,
                        "payment_status": payment_status,
                        "rationale": rationale,
                        "status_summary": status_summary,
                        "to_due_date": to_due_date,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_METRICS_METADATA,
            ),
        )

    async def pending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> BillSearchResult:
        """Get bills that are pending approval from the current user (post_agent_tool_api___get_bills_for_approval)."""
        return cast(
            BillSearchResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bills-for-approval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"limit": limit, "page_cursor": page_cursor, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_PENDING_METADATA,
            ),
        )

    async def recurring(
        self,
        *,
        rationale: str,
        recurring_bill_id: str,
    ) -> RecurringBillDetails:
        """Retrieve details of a recurring bill template including vendor, amount, recurrence schedule, and next payment date (post_agent_tool_api___get_recurring_bill)."""
        return cast(
            RecurringBillDetails,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-recurring-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "recurring_bill_id": recurring_bill_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_RECURRING_METADATA,
            ),
        )

    async def remind(
        self,
        *,
        bill_uuids: Sequence[UUID],
        rationale: str,
    ) -> BillApproverReminderResult:
        """Remind next approvers for bills awaiting approval (post_agent_tool_api___remind_bill_approvers)."""
        return cast(
            BillApproverReminderResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remind-bill-approvers",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"bill_uuids": bill_uuids, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_REMIND_METADATA,
            ),
        )

    async def search(
        self,
        *,
        accrual_year_month: str | None | NotGiven = NOT_GIVEN,
        from_due_date: str | None | NotGiven = NOT_GIVEN,
        from_payment_date: str | None | NotGiven = NOT_GIVEN,
        include_drafts: bool | None | NotGiven = NOT_GIVEN,
        include_paid: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        rationale: str,
        status_summaries: Sequence[str] | None | NotGiven = NOT_GIVEN,
        to_due_date: str | None | NotGiven = NOT_GIVEN,
        to_payment_date: str | None | NotGiven = NOT_GIVEN,
    ) -> BillSearchResult:
        """Search for bills using natural language queries like vendor names, amounts, or invoice numbers (post_agent_tool_api___search_bills)."""
        return cast(
            BillSearchResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-bills",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accrual_year_month": accrual_year_month,
                        "from_due_date": from_due_date,
                        "from_payment_date": from_payment_date,
                        "include_drafts": include_drafts,
                        "include_paid": include_paid,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "query": query,
                        "rationale": rationale,
                        "status_summaries": status_summaries,
                        "to_due_date": to_due_date,
                        "to_payment_date": to_payment_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_SEARCH_METADATA,
            ),
        )

    async def status(
        self,
        *,
        bill_id: str,
        rationale: str,
    ) -> BillStatus:
        """Get the current payment and approval status of a specific bill, including any required next actions (post_agent_tool_api___get_bill_status)."""
        return cast(
            BillStatus,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bill-status",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"bill_id": bill_id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_STATUS_METADATA,
            ),
        )

    async def submit(
        self,
        *,
        draft_bill_id: UUID,
        rationale: str,
    ) -> SubmitDraftBillResult:
        """Submit a ready draft bill for approval (post_agent_tool_api___submit_draft_bill)."""
        return cast(
            SubmitDraftBillResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-draft-bill",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"draft_bill_id": draft_bill_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BILLS_SUBMIT_METADATA,
            ),
        )


class AgentToolsBusiness:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        department_name: str,
        rationale: str,
    ) -> CreateDepartmentOutput:
        """Create a new department in the company (post_agent_tool_api___create_department)."""
        return cast(
            CreateDepartmentOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-department",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"department_name": department_name, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_CREATE_METADATA,
            ),
        )

    def departments(
        self,
        *,
        name_filter: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListDepartmentsOutput:
        """List all departments in the company (post_agent_tool_api___list_departments)."""
        return cast(
            ListDepartmentsOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/departments",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"name_filter": name_filter, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_DEPARTMENTS_METADATA,
            ),
        )

    def edit(
        self,
        *,
        department_id: str,
        department_name: str,
        rationale: str,
    ) -> RenameDepartmentOutput:
        """Rename an existing department in the company (post_agent_tool_api___rename_department)."""
        return cast(
            RenameDepartmentOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/rename-department",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_id": department_id,
                        "department_name": department_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_EDIT_METADATA,
            ),
        )

    def get(
        self,
        *,
        rationale: str,
    ) -> BusinessStatementDateResponse:
        """Get the business's statement billing schedule: the next statement close date, the configured statement close day of month, and the next card payment or autopay debit date (get_agent_tool_api___get_business_statement_date_tool)."""
        return cast(
            BusinessStatementDateResponse,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-business-statement-date",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_GET_METADATA,
            ),
        )


class AsyncAgentToolsBusiness:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        department_name: str,
        rationale: str,
    ) -> CreateDepartmentOutput:
        """Create a new department in the company (post_agent_tool_api___create_department)."""
        return cast(
            CreateDepartmentOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-department",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"department_name": department_name, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_CREATE_METADATA,
            ),
        )

    async def departments(
        self,
        *,
        name_filter: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListDepartmentsOutput:
        """List all departments in the company (post_agent_tool_api___list_departments)."""
        return cast(
            ListDepartmentsOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/departments",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"name_filter": name_filter, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_DEPARTMENTS_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        department_id: str,
        department_name: str,
        rationale: str,
    ) -> RenameDepartmentOutput:
        """Rename an existing department in the company (post_agent_tool_api___rename_department)."""
        return cast(
            RenameDepartmentOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/rename-department",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_id": department_id,
                        "department_name": department_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_EDIT_METADATA,
            ),
        )

    async def get(
        self,
        *,
        rationale: str,
    ) -> BusinessStatementDateResponse:
        """Get the business's statement billing schedule: the next statement close date, the configured statement close day of month, and the next card payment or autopay debit date (get_agent_tool_api___get_business_statement_date_tool)."""
        return cast(
            BusinessStatementDateResponse,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-business-statement-date",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_BUSINESS_GET_METADATA,
            ),
        )


class AgentToolsCards:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def activate(
        self,
        *,
        confirm_delivery: bool | NotGiven = NOT_GIVEN,
        last_four: str,
        rationale: str,
    ) -> CardActivationResult:
        """Activate a card by its last four digits (post_agent_tool_api___activate_card)."""
        return cast(
            CardActivationResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/activate-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirm_delivery": confirm_delivery,
                        "last_four": last_four,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_ACTIVATE_METADATA,
            ),
        )

    def list(
        self,
        *,
        cardholder_user_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> CardInfoList:
        """List non-terminated cards for the current user or a visible target cardholder, including activation status, lock state, and shipping metadata (post_agent_tool_api___list_cards)."""
        return cast(
            CardInfoList,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-cards",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "cardholder_user_uuid": cardholder_user_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_LIST_METADATA,
            ),
        )

    def lock(
        self,
        *,
        action: str,
        id: UUID,
        rationale: str,
    ) -> CardLockResult:
        """Lock or unlock a card the acting user is authorized to manage (post_agent_tool_api___lock_or_unlock_card)."""
        return cast(
            CardLockResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"action": action, "id": id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_LOCK_METADATA,
            ),
        )

    def unlock_fraud_locked_card(
        self,
        *,
        id: str,
        rationale: str,
        user_confirmed_fraud_whitelist: bool | NotGiven = NOT_GIVEN,
    ) -> CardUnlockResult:
        """Unlock a card that was locked due to a suspicious transaction (post_agent_tool_api___unlock_fraud_locked_card)."""
        return cast(
            CardUnlockResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/unlock-fraud-locked-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "id": id,
                        "rationale": rationale,
                        "user_confirmed_fraud_whitelist": user_confirmed_fraud_whitelist,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_UNLOCK_FRAUD_LOCKED_CARD_METADATA,
            ),
        )


class AsyncAgentToolsCards:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def activate(
        self,
        *,
        confirm_delivery: bool | NotGiven = NOT_GIVEN,
        last_four: str,
        rationale: str,
    ) -> CardActivationResult:
        """Activate a card by its last four digits (post_agent_tool_api___activate_card)."""
        return cast(
            CardActivationResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/activate-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirm_delivery": confirm_delivery,
                        "last_four": last_four,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_ACTIVATE_METADATA,
            ),
        )

    async def list(
        self,
        *,
        cardholder_user_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> CardInfoList:
        """List non-terminated cards for the current user or a visible target cardholder, including activation status, lock state, and shipping metadata (post_agent_tool_api___list_cards)."""
        return cast(
            CardInfoList,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-cards",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "cardholder_user_uuid": cardholder_user_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_LIST_METADATA,
            ),
        )

    async def lock(
        self,
        *,
        action: str,
        id: UUID,
        rationale: str,
    ) -> CardLockResult:
        """Lock or unlock a card the acting user is authorized to manage (post_agent_tool_api___lock_or_unlock_card)."""
        return cast(
            CardLockResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"action": action, "id": id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_LOCK_METADATA,
            ),
        )

    async def unlock_fraud_locked_card(
        self,
        *,
        id: str,
        rationale: str,
        user_confirmed_fraud_whitelist: bool | NotGiven = NOT_GIVEN,
    ) -> CardUnlockResult:
        """Unlock a card that was locked due to a suspicious transaction (post_agent_tool_api___unlock_fraud_locked_card)."""
        return cast(
            CardUnlockResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/unlock-fraud-locked-card",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "id": id,
                        "rationale": rationale,
                        "user_confirmed_fraud_whitelist": user_confirmed_fraud_whitelist,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_CARDS_UNLOCK_FRAUD_LOCKED_CARD_METADATA,
            ),
        )


class AgentToolsCommunication:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def comment(
        self,
        *,
        mention_user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        message: str,
        ramp_object_type: str,
        ramp_object_uuid: str,
        rationale: str,
    ) -> CommentPosted:
        """Post a comment on a Ramp object (transaction, bill, reimbursement, etc) (post_agent_tool_api___post_comment)."""
        return cast(
            CommentPosted,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/post-comment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "mention_user_uuids": mention_user_uuids,
                        "message": message,
                        "ramp_object_type": ramp_object_type,
                        "ramp_object_uuid": ramp_object_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_COMMUNICATION_COMMENT_METADATA,
            ),
        )


class AsyncAgentToolsCommunication:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def comment(
        self,
        *,
        mention_user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        message: str,
        ramp_object_type: str,
        ramp_object_uuid: str,
        rationale: str,
    ) -> CommentPosted:
        """Post a comment on a Ramp object (transaction, bill, reimbursement, etc) (post_agent_tool_api___post_comment)."""
        return cast(
            CommentPosted,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/post-comment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "mention_user_uuids": mention_user_uuids,
                        "message": message,
                        "ramp_object_type": ramp_object_type,
                        "ramp_object_uuid": ramp_object_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_COMMUNICATION_COMMENT_METADATA,
            ),
        )


class AgentToolsDeclines:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def explain(
        self,
        *,
        rationale: str,
        transaction_uuid: str,
    ) -> DeclineExplanation:
        """Get a detailed explanation of why a card transaction was declined (post_agent_tool_api___get_decline_explanation)."""
        return cast(
            DeclineExplanation,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-decline-explanation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "transaction_uuid": transaction_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_DECLINES_EXPLAIN_METADATA,
            ),
        )


class AsyncAgentToolsDeclines:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def explain(
        self,
        *,
        rationale: str,
        transaction_uuid: str,
    ) -> DeclineExplanation:
        """Get a detailed explanation of why a card transaction was declined (post_agent_tool_api___get_decline_explanation)."""
        return cast(
            DeclineExplanation,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-decline-explanation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "transaction_uuid": transaction_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_DECLINES_EXPLAIN_METADATA,
            ),
        )


class AgentToolsExternalAgents:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get_more_tools(
        self,
        *,
        context: str,
        rationale: str,
    ) -> GetMoreToolsResult:
        """Report a capability that is missing from the available Ramp tools (post_agent_tool_api___get_more_tools)."""
        return cast(
            GetMoreToolsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-more-tools",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"context": context, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_EXTERNAL_AGENTS_GET_MORE_TOOLS_METADATA,
            ),
        )


class AsyncAgentToolsExternalAgents:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get_more_tools(
        self,
        *,
        context: str,
        rationale: str,
    ) -> GetMoreToolsResult:
        """Report a capability that is missing from the available Ramp tools (post_agent_tool_api___get_more_tools)."""
        return cast(
            GetMoreToolsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-more-tools",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"context": context, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_EXTERNAL_AGENTS_GET_MORE_TOOLS_METADATA,
            ),
        )


class AgentToolsFunds:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def add_user(
        self,
        *,
        enable_sharing_if_needed: bool | NotGiven = NOT_GIVEN,
        rationale: str,
        role: str | NotGiven = NOT_GIVEN,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> AddUserToSharedFundPublicResult:
        """Add a user to a shared fund as a member or co-owner (post_agent_tool_api___add_user_to_shared_fund)."""
        return cast(
            AddUserToSharedFundPublicResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/add-user-to-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "enable_sharing_if_needed": enable_sharing_if_needed,
                        "rationale": rationale,
                        "role": role,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ADD_USER_METADATA,
            ),
        )

    def archive(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> ArchiveSpendAllocationOutput:
        """Archive a fund to prevent spend and hide it from users (post_agent_tool_api___archive_spend_allocation_tool)."""
        return cast(
            ArchiveSpendAllocationOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/archive-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ARCHIVE_METADATA,
            ),
        )

    def create(
        self,
        *,
        amount: str,
        categories_blacklist: Sequence[int] | None | NotGiven = NOT_GIVEN,
        categories_whitelist: Sequence[int] | None | NotGiven = NOT_GIVEN,
        default_member_limit_amount: str | None | NotGiven = NOT_GIVEN,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        display_name: str,
        dynamic_user_group_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        is_shareable: bool | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        lock_date: str | None | NotGiven = NOT_GIVEN,
        member_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        rationale: str,
        user_custom_field_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        user_ids: Sequence[str],
        vendor_blacklist: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
        vendor_whitelist: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
    ) -> IssueOneOffFundsResult:
        """Issue one-off funds (spend allocations) directly, bypassing approval flows (post_agent_tool_api___issue_one_off_funds)."""
        return cast(
            IssueOneOffFundsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/issue-one-off-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "categories_blacklist": categories_blacklist,
                        "categories_whitelist": categories_whitelist,
                        "default_member_limit_amount": default_member_limit_amount,
                        "department_ids": department_ids,
                        "display_name": display_name,
                        "dynamic_user_group_ids": dynamic_user_group_ids,
                        "interval": interval,
                        "is_shareable": is_shareable,
                        "location_ids": location_ids,
                        "lock_date": lock_date,
                        "member_ids": member_ids,
                        "rationale": rationale,
                        "user_custom_field_ids": user_custom_field_ids,
                        "user_ids": user_ids,
                        "vendor_blacklist": vendor_blacklist,
                        "vendor_whitelist": vendor_whitelist,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_CREATE_METADATA,
            ),
        )

    def delete(
        self,
        *,
        rationale: str,
        spend_intent_delete_action: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: str,
        transfer_to_spend_intent_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> DeleteSpendProgramResult:
        """Delete (terminate) a spend program (post_agent_tool_api___delete_spend_program)."""
        return cast(
            DeleteSpendProgramResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/delete-spend-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_intent_delete_action": spend_intent_delete_action,
                        "spend_intent_uuid": spend_intent_uuid,
                        "transfer_to_spend_intent_uuid": transfer_to_spend_intent_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_DELETE_METADATA,
            ),
        )

    def edit(
        self,
        *,
        action: str | NotGiven = NOT_GIVEN,
        amount: Any,
        card_id: str | None | NotGiven = NOT_GIVEN,
        increase_type: str | NotGiven = NOT_GIVEN,
        rationale: str,
        spend_allocation_id: str | None | NotGiven = NOT_GIVEN,
        user_confirmed_increase_type: bool | NotGiven = NOT_GIVEN,
        user_confirmed_limit_increase: bool | NotGiven = NOT_GIVEN,
    ) -> LimitIncreaseResult:
        """Increase the spending limit on a fund (spend allocation) or card (post_agent_tool_api___limit_increase)."""
        return cast(
            LimitIncreaseResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/limit-increase",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "amount": amount,
                        "card_id": card_id,
                        "increase_type": increase_type,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                        "user_confirmed_increase_type": user_confirmed_increase_type,
                        "user_confirmed_limit_increase": user_confirmed_limit_increase,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_EDIT_METADATA,
            ),
        )

    def edit_user_role(
        self,
        *,
        new_role: str,
        rationale: str,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> EditUserRoleOnSharedFundPublicResult:
        """Change a shared-fund user's role between member and co-owner using user_email (post_agent_tool_api___edit_user_role_on_shared_fund)."""
        return cast(
            EditUserRoleOnSharedFundPublicResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-user-role-on-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "new_role": new_role,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_EDIT_USER_ROLE_METADATA,
            ),
        )

    def enable_shared(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> EnableSharedFundAccessResult:
        """Enable sharing on an existing fund so members can be added to it (post_agent_tool_api___enable_shared_fund_access)."""
        return cast(
            EnableSharedFundAccessResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/enable-shared-fund-access",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ENABLE_SHARED_METADATA,
            ),
        )

    def issue_from_program(
        self,
        *,
        department_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        display_name: str | None | NotGiven = NOT_GIVEN,
        dynamic_user_group_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        issue_to_all_users: bool | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        lock_date: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        spend_amount: str | None | NotGiven = NOT_GIVEN,
        spend_currency: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: str,
        spend_interval: str | None | NotGiven = NOT_GIVEN,
        user_custom_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        user_ids: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> IssueFromSpendProgramResult:
        """Issue spend allocations from an existing spend program (post_agent_tool_api___issue_from_spend_program)."""
        return cast(
            IssueFromSpendProgramResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/issue-from-spend-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_ids": department_ids,
                        "display_name": display_name,
                        "dynamic_user_group_ids": dynamic_user_group_ids,
                        "issue_to_all_users": issue_to_all_users,
                        "location_ids": location_ids,
                        "lock_date": lock_date,
                        "rationale": rationale,
                        "spend_amount": spend_amount,
                        "spend_currency": spend_currency,
                        "spend_intent_uuid": spend_intent_uuid,
                        "spend_interval": spend_interval,
                        "user_custom_field_ids": user_custom_field_ids,
                        "user_ids": user_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ISSUE_FROM_PROGRAM_METADATA,
            ),
        )

    def list(
        self,
        *,
        agent_card_eligible: bool | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        for_transaction_id: str | None | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        funds_to_retrieve: str | None | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_lock_info: bool | NotGiven = NOT_GIVEN,
        include_members: bool | NotGiven = NOT_GIVEN,
        include_restrictions: bool | NotGiven = NOT_GIVEN,
        is_shared: bool | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_by_fund_display_name: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        state: str | None | NotGiven = NOT_GIVEN,
        user_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
    ) -> UserFunds:
        """Retrieve funds (cards or budgets) and their balances, restrictions, locks, owners, (post_agent_tool_api___get_user_funds)."""
        return cast(
            UserFunds,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "agent_card_eligible": agent_card_eligible,
                        "cursor": cursor,
                        "for_transaction_id": for_transaction_id,
                        "fund_uuid": fund_uuid,
                        "funds_to_retrieve": funds_to_retrieve,
                        "include_balance": include_balance,
                        "include_lock_info": include_lock_info,
                        "include_members": include_members,
                        "include_restrictions": include_restrictions,
                        "is_shared": is_shared,
                        "page_size": page_size,
                        "rationale": rationale,
                        "search_by_fund_display_name": search_by_fund_display_name,
                        "spend_intent_uuids": spend_intent_uuids,
                        "state": state,
                        "user_uuids": user_uuids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LIST_METADATA,
            ),
        )

    def lock(
        self,
        *,
        action: str,
        id: str,
        rationale: str,
    ) -> LockOrUnlockSpendAllocationResult:
        """Lock or unlock a fund (spend allocation) at the fund level, affecting all members (post_agent_tool_api___lock_or_unlock_spend_allocation)."""
        return cast(
            LockOrUnlockSpendAllocationResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"action": action, "id": id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LOCK_METADATA,
            ),
        )

    def lock_or_unlock_spend_allocation_member(
        self,
        *,
        action: str,
        id: str,
        member_id: str,
        rationale: str,
    ) -> LockOrUnlockSpendAllocationMemberResult:
        """Lock or unlock a specific member's access to a fund (spend allocation) (post_agent_tool_api___lock_or_unlock_spend_allocation_member)."""
        return cast(
            LockOrUnlockSpendAllocationMemberResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-spend-allocation-member",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "id": id,
                        "member_id": member_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LOCK_OR_UNLOCK_SPEND_ALLOCATION_MEMBER_METADATA,
            ),
        )

    def remove_user(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> RemoveUserFromSharedFundPublicResult:
        """Remove a user from a shared fund using user_email (post_agent_tool_api___remove_user_from_shared_fund)."""
        return cast(
            RemoveUserFromSharedFundPublicResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remove-user-from-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_REMOVE_USER_METADATA,
            ),
        )

    def request_funds(
        self,
        *,
        amount: Any | None | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        frequency: str | None | NotGiven = NOT_GIVEN,
        name: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        request_type: str | NotGiven = NOT_GIVEN,
    ) -> FundRequestLink:
        """Build a prefilled link for a NEW fund/card request (post_agent_tool_api___create_fund_request)."""
        return cast(
            FundRequestLink,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-fund-request",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency": currency,
                        "description": description,
                        "frequency": frequency,
                        "name": name,
                        "rationale": rationale,
                        "request_type": request_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_REQUEST_FUNDS_METADATA,
            ),
        )

    def set_decline_buffer(
        self,
        *,
        allowed_overage_percent: Any | None,
        buffer_application_mode: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        target_id: str | None | NotGiven = NOT_GIVEN,
        target_type: str,
    ) -> SetDeclineBufferResult:
        """Set or clear decline buffer percentages for business settings, spend programs, or funds (post_agent_tool_api___set_decline_buffer)."""
        return cast(
            SetDeclineBufferResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-decline-buffer",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "allowed_overage_percent": allowed_overage_percent,
                        "buffer_application_mode": buffer_application_mode,
                        "rationale": rationale,
                        "target_id": target_id,
                        "target_type": target_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_SET_DECLINE_BUFFER_METADATA,
            ),
        )

    def transfer_ownership(
        self,
        *,
        current_user_email: str,
        new_user_email: str,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> TransferSpendAllocationOwnershipPublicResult:
        """Transfer ownership of a spend allocation using the current and new owners' emails (post_agent_tool_api___transfer_spend_allocation_ownership)."""
        return cast(
            TransferSpendAllocationOwnershipPublicResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/transfer-spend-allocation-ownership",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "current_user_email": current_user_email,
                        "new_user_email": new_user_email,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_TRANSFER_OWNERSHIP_METADATA,
            ),
        )

    def unarchive(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> UnarchiveSpendAllocationOutput:
        """Unarchive a fund so it becomes visible and spendable again (post_agent_tool_api___unarchive_spend_allocation_tool)."""
        return cast(
            UnarchiveSpendAllocationOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/unarchive-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UNARCHIVE_METADATA,
            ),
        )

    def update_category_restrictions(
        self,
        *,
        action: str,
        category_ids: Sequence[int],
        rationale: str,
        spend_allocation_id: str,
    ) -> UpdateCategoryRestrictionsResult:
        """Update spending category restrictions (whitelist or blacklist) on a single fund (post_agent_tool_api___update_category_restrictions)."""
        return cast(
            UpdateCategoryRestrictionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-category-restrictions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "category_ids": category_ids,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_CATEGORY_RESTRICTIONS_METADATA,
            ),
        )

    def update_interval(
        self,
        *,
        interval: str,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> UpdateSpendAllocationIntervalOutput:
        """Update only the spend interval for a spend allocation (post_agent_tool_api___update_spend_allocation_interval_tool)."""
        return cast(
            UpdateSpendAllocationIntervalOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-spend-allocation-interval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "interval": interval,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_INTERVAL_METADATA,
            ),
        )

    def update_merchant_restrictions(
        self,
        *,
        action: str,
        merchant_uuids: Sequence[str],
        rationale: str,
        restriction_type: str,
        spend_allocation_id: str,
    ) -> UpdateMerchantRestrictionsResult:
        """Update merchant restrictions (whitelist or blacklist) on a fund (spend allocation) (post_agent_tool_api___update_merchant_restrictions)."""
        return cast(
            UpdateMerchantRestrictionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-merchant-restrictions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "merchant_uuids": merchant_uuids,
                        "rationale": rationale,
                        "restriction_type": restriction_type,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_MERCHANT_RESTRICTIONS_METADATA,
            ),
        )

    def update_transaction_amount_limit(
        self,
        *,
        card_id: str | None | NotGiven = NOT_GIVEN,
        new_transaction_amount_limit: Any,
        rationale: str,
        spend_allocation_id: str | None | NotGiven = NOT_GIVEN,
    ) -> UpdateTransactionAmountLimitResult:
        """Set a fund's maximum amount for one transaction (post_agent_tool_api___update_transaction_amount_limit)."""
        return cast(
            UpdateTransactionAmountLimitResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-transaction-amount-limit",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "card_id": card_id,
                        "new_transaction_amount_limit": new_transaction_amount_limit,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_TRANSACTION_AMOUNT_LIMIT_METADATA,
            ),
        )


class AsyncAgentToolsFunds:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def add_user(
        self,
        *,
        enable_sharing_if_needed: bool | NotGiven = NOT_GIVEN,
        rationale: str,
        role: str | NotGiven = NOT_GIVEN,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> AddUserToSharedFundPublicResult:
        """Add a user to a shared fund as a member or co-owner (post_agent_tool_api___add_user_to_shared_fund)."""
        return cast(
            AddUserToSharedFundPublicResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/add-user-to-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "enable_sharing_if_needed": enable_sharing_if_needed,
                        "rationale": rationale,
                        "role": role,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ADD_USER_METADATA,
            ),
        )

    async def archive(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> ArchiveSpendAllocationOutput:
        """Archive a fund to prevent spend and hide it from users (post_agent_tool_api___archive_spend_allocation_tool)."""
        return cast(
            ArchiveSpendAllocationOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/archive-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ARCHIVE_METADATA,
            ),
        )

    async def create(
        self,
        *,
        amount: str,
        categories_blacklist: Sequence[int] | None | NotGiven = NOT_GIVEN,
        categories_whitelist: Sequence[int] | None | NotGiven = NOT_GIVEN,
        default_member_limit_amount: str | None | NotGiven = NOT_GIVEN,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        display_name: str,
        dynamic_user_group_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        interval: str | NotGiven = NOT_GIVEN,
        is_shareable: bool | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        lock_date: str | None | NotGiven = NOT_GIVEN,
        member_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        rationale: str,
        user_custom_field_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        user_ids: Sequence[str],
        vendor_blacklist: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
        vendor_whitelist: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
    ) -> IssueOneOffFundsResult:
        """Issue one-off funds (spend allocations) directly, bypassing approval flows (post_agent_tool_api___issue_one_off_funds)."""
        return cast(
            IssueOneOffFundsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/issue-one-off-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "categories_blacklist": categories_blacklist,
                        "categories_whitelist": categories_whitelist,
                        "default_member_limit_amount": default_member_limit_amount,
                        "department_ids": department_ids,
                        "display_name": display_name,
                        "dynamic_user_group_ids": dynamic_user_group_ids,
                        "interval": interval,
                        "is_shareable": is_shareable,
                        "location_ids": location_ids,
                        "lock_date": lock_date,
                        "member_ids": member_ids,
                        "rationale": rationale,
                        "user_custom_field_ids": user_custom_field_ids,
                        "user_ids": user_ids,
                        "vendor_blacklist": vendor_blacklist,
                        "vendor_whitelist": vendor_whitelist,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_CREATE_METADATA,
            ),
        )

    async def delete(
        self,
        *,
        rationale: str,
        spend_intent_delete_action: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: str,
        transfer_to_spend_intent_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> DeleteSpendProgramResult:
        """Delete (terminate) a spend program (post_agent_tool_api___delete_spend_program)."""
        return cast(
            DeleteSpendProgramResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/delete-spend-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_intent_delete_action": spend_intent_delete_action,
                        "spend_intent_uuid": spend_intent_uuid,
                        "transfer_to_spend_intent_uuid": transfer_to_spend_intent_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_DELETE_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        action: str | NotGiven = NOT_GIVEN,
        amount: Any,
        card_id: str | None | NotGiven = NOT_GIVEN,
        increase_type: str | NotGiven = NOT_GIVEN,
        rationale: str,
        spend_allocation_id: str | None | NotGiven = NOT_GIVEN,
        user_confirmed_increase_type: bool | NotGiven = NOT_GIVEN,
        user_confirmed_limit_increase: bool | NotGiven = NOT_GIVEN,
    ) -> LimitIncreaseResult:
        """Increase the spending limit on a fund (spend allocation) or card (post_agent_tool_api___limit_increase)."""
        return cast(
            LimitIncreaseResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/limit-increase",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "amount": amount,
                        "card_id": card_id,
                        "increase_type": increase_type,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                        "user_confirmed_increase_type": user_confirmed_increase_type,
                        "user_confirmed_limit_increase": user_confirmed_limit_increase,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_EDIT_METADATA,
            ),
        )

    async def edit_user_role(
        self,
        *,
        new_role: str,
        rationale: str,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> EditUserRoleOnSharedFundPublicResult:
        """Change a shared-fund user's role between member and co-owner using user_email (post_agent_tool_api___edit_user_role_on_shared_fund)."""
        return cast(
            EditUserRoleOnSharedFundPublicResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-user-role-on-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "new_role": new_role,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_EDIT_USER_ROLE_METADATA,
            ),
        )

    async def enable_shared(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> EnableSharedFundAccessResult:
        """Enable sharing on an existing fund so members can be added to it (post_agent_tool_api___enable_shared_fund_access)."""
        return cast(
            EnableSharedFundAccessResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/enable-shared-fund-access",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ENABLE_SHARED_METADATA,
            ),
        )

    async def issue_from_program(
        self,
        *,
        department_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        display_name: str | None | NotGiven = NOT_GIVEN,
        dynamic_user_group_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        issue_to_all_users: bool | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        lock_date: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        spend_amount: str | None | NotGiven = NOT_GIVEN,
        spend_currency: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: str,
        spend_interval: str | None | NotGiven = NOT_GIVEN,
        user_custom_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        user_ids: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> IssueFromSpendProgramResult:
        """Issue spend allocations from an existing spend program (post_agent_tool_api___issue_from_spend_program)."""
        return cast(
            IssueFromSpendProgramResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/issue-from-spend-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_ids": department_ids,
                        "display_name": display_name,
                        "dynamic_user_group_ids": dynamic_user_group_ids,
                        "issue_to_all_users": issue_to_all_users,
                        "location_ids": location_ids,
                        "lock_date": lock_date,
                        "rationale": rationale,
                        "spend_amount": spend_amount,
                        "spend_currency": spend_currency,
                        "spend_intent_uuid": spend_intent_uuid,
                        "spend_interval": spend_interval,
                        "user_custom_field_ids": user_custom_field_ids,
                        "user_ids": user_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_ISSUE_FROM_PROGRAM_METADATA,
            ),
        )

    async def list(
        self,
        *,
        agent_card_eligible: bool | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        for_transaction_id: str | None | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        funds_to_retrieve: str | None | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_lock_info: bool | NotGiven = NOT_GIVEN,
        include_members: bool | NotGiven = NOT_GIVEN,
        include_restrictions: bool | NotGiven = NOT_GIVEN,
        is_shared: bool | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_by_fund_display_name: str | None | NotGiven = NOT_GIVEN,
        spend_intent_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        state: str | None | NotGiven = NOT_GIVEN,
        user_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
    ) -> UserFunds:
        """Retrieve funds (cards or budgets) and their balances, restrictions, locks, owners, (post_agent_tool_api___get_user_funds)."""
        return cast(
            UserFunds,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-funds",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "agent_card_eligible": agent_card_eligible,
                        "cursor": cursor,
                        "for_transaction_id": for_transaction_id,
                        "fund_uuid": fund_uuid,
                        "funds_to_retrieve": funds_to_retrieve,
                        "include_balance": include_balance,
                        "include_lock_info": include_lock_info,
                        "include_members": include_members,
                        "include_restrictions": include_restrictions,
                        "is_shared": is_shared,
                        "page_size": page_size,
                        "rationale": rationale,
                        "search_by_fund_display_name": search_by_fund_display_name,
                        "spend_intent_uuids": spend_intent_uuids,
                        "state": state,
                        "user_uuids": user_uuids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LIST_METADATA,
            ),
        )

    async def lock(
        self,
        *,
        action: str,
        id: str,
        rationale: str,
    ) -> LockOrUnlockSpendAllocationResult:
        """Lock or unlock a fund (spend allocation) at the fund level, affecting all members (post_agent_tool_api___lock_or_unlock_spend_allocation)."""
        return cast(
            LockOrUnlockSpendAllocationResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"action": action, "id": id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LOCK_METADATA,
            ),
        )

    async def lock_or_unlock_spend_allocation_member(
        self,
        *,
        action: str,
        id: str,
        member_id: str,
        rationale: str,
    ) -> LockOrUnlockSpendAllocationMemberResult:
        """Lock or unlock a specific member's access to a fund (spend allocation) (post_agent_tool_api___lock_or_unlock_spend_allocation_member)."""
        return cast(
            LockOrUnlockSpendAllocationMemberResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/lock-or-unlock-spend-allocation-member",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "id": id,
                        "member_id": member_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_LOCK_OR_UNLOCK_SPEND_ALLOCATION_MEMBER_METADATA,
            ),
        )

    async def remove_user(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
        user_email: str,
    ) -> RemoveUserFromSharedFundPublicResult:
        """Remove a user from a shared fund using user_email (post_agent_tool_api___remove_user_from_shared_fund)."""
        return cast(
            RemoveUserFromSharedFundPublicResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remove-user-from-shared-fund",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                        "user_email": user_email,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_REMOVE_USER_METADATA,
            ),
        )

    async def request_funds(
        self,
        *,
        amount: Any | None | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        frequency: str | None | NotGiven = NOT_GIVEN,
        name: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        request_type: str | NotGiven = NOT_GIVEN,
    ) -> FundRequestLink:
        """Build a prefilled link for a NEW fund/card request (post_agent_tool_api___create_fund_request)."""
        return cast(
            FundRequestLink,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-fund-request",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency": currency,
                        "description": description,
                        "frequency": frequency,
                        "name": name,
                        "rationale": rationale,
                        "request_type": request_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_REQUEST_FUNDS_METADATA,
            ),
        )

    async def set_decline_buffer(
        self,
        *,
        allowed_overage_percent: Any | None,
        buffer_application_mode: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        target_id: str | None | NotGiven = NOT_GIVEN,
        target_type: str,
    ) -> SetDeclineBufferResult:
        """Set or clear decline buffer percentages for business settings, spend programs, or funds (post_agent_tool_api___set_decline_buffer)."""
        return cast(
            SetDeclineBufferResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-decline-buffer",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "allowed_overage_percent": allowed_overage_percent,
                        "buffer_application_mode": buffer_application_mode,
                        "rationale": rationale,
                        "target_id": target_id,
                        "target_type": target_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_SET_DECLINE_BUFFER_METADATA,
            ),
        )

    async def transfer_ownership(
        self,
        *,
        current_user_email: str,
        new_user_email: str,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> TransferSpendAllocationOwnershipPublicResult:
        """Transfer ownership of a spend allocation using the current and new owners' emails (post_agent_tool_api___transfer_spend_allocation_ownership)."""
        return cast(
            TransferSpendAllocationOwnershipPublicResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/transfer-spend-allocation-ownership",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "current_user_email": current_user_email,
                        "new_user_email": new_user_email,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_TRANSFER_OWNERSHIP_METADATA,
            ),
        )

    async def unarchive(
        self,
        *,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> UnarchiveSpendAllocationOutput:
        """Unarchive a fund so it becomes visible and spendable again (post_agent_tool_api___unarchive_spend_allocation_tool)."""
        return cast(
            UnarchiveSpendAllocationOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/unarchive-spend-allocation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UNARCHIVE_METADATA,
            ),
        )

    async def update_category_restrictions(
        self,
        *,
        action: str,
        category_ids: Sequence[int],
        rationale: str,
        spend_allocation_id: str,
    ) -> UpdateCategoryRestrictionsResult:
        """Update spending category restrictions (whitelist or blacklist) on a single fund (post_agent_tool_api___update_category_restrictions)."""
        return cast(
            UpdateCategoryRestrictionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-category-restrictions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "category_ids": category_ids,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_CATEGORY_RESTRICTIONS_METADATA,
            ),
        )

    async def update_interval(
        self,
        *,
        interval: str,
        rationale: str,
        spend_allocation_uuid: str,
    ) -> UpdateSpendAllocationIntervalOutput:
        """Update only the spend interval for a spend allocation (post_agent_tool_api___update_spend_allocation_interval_tool)."""
        return cast(
            UpdateSpendAllocationIntervalOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-spend-allocation-interval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "interval": interval,
                        "rationale": rationale,
                        "spend_allocation_uuid": spend_allocation_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_INTERVAL_METADATA,
            ),
        )

    async def update_merchant_restrictions(
        self,
        *,
        action: str,
        merchant_uuids: Sequence[str],
        rationale: str,
        restriction_type: str,
        spend_allocation_id: str,
    ) -> UpdateMerchantRestrictionsResult:
        """Update merchant restrictions (whitelist or blacklist) on a fund (spend allocation) (post_agent_tool_api___update_merchant_restrictions)."""
        return cast(
            UpdateMerchantRestrictionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-merchant-restrictions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "merchant_uuids": merchant_uuids,
                        "rationale": rationale,
                        "restriction_type": restriction_type,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_MERCHANT_RESTRICTIONS_METADATA,
            ),
        )

    async def update_transaction_amount_limit(
        self,
        *,
        card_id: str | None | NotGiven = NOT_GIVEN,
        new_transaction_amount_limit: Any,
        rationale: str,
        spend_allocation_id: str | None | NotGiven = NOT_GIVEN,
    ) -> UpdateTransactionAmountLimitResult:
        """Set a fund's maximum amount for one transaction (post_agent_tool_api___update_transaction_amount_limit)."""
        return cast(
            UpdateTransactionAmountLimitResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-transaction-amount-limit",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "card_id": card_id,
                        "new_transaction_amount_limit": new_transaction_amount_limit,
                        "rationale": rationale,
                        "spend_allocation_id": spend_allocation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_FUNDS_UPDATE_TRANSACTION_AMOUNT_LIMIT_METADATA,
            ),
        )


class AgentToolsGeneral:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def agent_nps_submit(
        self,
        *,
        explanation: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        score: int,
        survey_token: str,
    ) -> SubmitAgentNpsResult:
        """Submit an optional Agent NPS response using a one-time survey token (post_agent_tool_api___submit_agent_nps)."""
        return cast(
            SubmitAgentNpsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit_agent_nps",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "explanation": explanation,
                        "rationale": rationale,
                        "score": score,
                        "survey_token": survey_token,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_GENERAL_AGENT_NPS_SUBMIT_METADATA,
            ),
        )


class AsyncAgentToolsGeneral:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def agent_nps_submit(
        self,
        *,
        explanation: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        score: int,
        survey_token: str,
    ) -> SubmitAgentNpsResult:
        """Submit an optional Agent NPS response using a one-time survey token (post_agent_tool_api___submit_agent_nps)."""
        return cast(
            SubmitAgentNpsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit_agent_nps",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "explanation": explanation,
                        "rationale": rationale,
                        "score": score,
                        "survey_token": survey_token,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_GENERAL_AGENT_NPS_SUBMIT_METADATA,
            ),
        )


class AgentToolsMerchant:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def categories(
        self,
        *,
        rationale: str,
    ) -> ListSkCategoriesResult:
        """List all available spend categories (post_agent_tool_api___list_sk_categories)."""
        return cast(
            ListSkCategoriesResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/merchant-categories",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_MERCHANT_CATEGORIES_METADATA,
            ),
        )

    def search(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        query: str,
        rationale: str,
    ) -> SearchMerchantsResult:
        """Search for merchants by name (post_agent_tool_api___search_merchants)."""
        return cast(
            SearchMerchantsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-merchants",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"limit": limit, "query": query, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_MERCHANT_SEARCH_METADATA,
            ),
        )


class AsyncAgentToolsMerchant:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def categories(
        self,
        *,
        rationale: str,
    ) -> ListSkCategoriesResult:
        """List all available spend categories (post_agent_tool_api___list_sk_categories)."""
        return cast(
            ListSkCategoriesResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/merchant-categories",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_MERCHANT_CATEGORIES_METADATA,
            ),
        )

    async def search(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        query: str,
        rationale: str,
    ) -> SearchMerchantsResult:
        """Search for merchants by name (post_agent_tool_api___search_merchants)."""
        return cast(
            SearchMerchantsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-merchants",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"limit": limit, "query": query, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_MERCHANT_SEARCH_METADATA,
            ),
        )


class AgentToolsPolicy:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def body(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
        workflow_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetPolicyWorkflowBodyPublicSuccess:
        """Fetch the published (or a specific historical) workflow body for a workflow-backed policy, including compact branch structure, condition operands, and a workflow outline of the visible builder steps (get_agent_tool_api___get_policy_workflow_body)."""
        return cast(
            GetPolicyWorkflowBodyPublicSuccess,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-policy-workflow-body",
                path_params=None,
                params=_without_not_given(
                    {
                        "kind": kind,
                        "policy_uuid": policy_uuid,
                        "rationale": rationale,
                        "workflow_uuid": workflow_uuid,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_BODY_METADATA,
            ),
        )

    def explain(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetExpenseWorkflowContextSuccess:
        """Resolve a transaction or reimbursement UUID to its approval workflow context: the expense summary, its approval chain steps and approvers, the attached approval and submission policies, any travel booking approval, and the latest Policy Agent review (get_agent_tool_api___get_expense_workflow_context)."""
        return cast(
            GetExpenseWorkflowContextSuccess,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-expense-workflow-context",
                path_params=None,
                params=_without_not_given(
                    {
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_EXPLAIN_METADATA,
            ),
        )

    def get(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
    ) -> PolicyDetailsSuccess:
        """Fetch detailed metadata for one workflow-backed policy by UUID, including display name, spend type, default status, and separation-of-duties configuration (get_agent_tool_api___get_policy_details)."""
        return cast(
            PolicyDetailsSuccess,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-policy-details",
                path_params=None,
                params=_without_not_given(
                    {"kind": kind, "policy_uuid": policy_uuid, "rationale": rationale}
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_GET_METADATA,
            ),
        )

    def list(
        self,
        *,
        kinds: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListPoliciesSuccess:
        """List workflow-backed submission, approval, and spend-request policies for the business, with each policy's UUID, kind, spend type, default status, and workflow availability (get_agent_tool_api___list_policies)."""
        return cast(
            ListPoliciesSuccess,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-policies",
                path_params=None,
                params=_without_not_given({"kinds": kinds, "rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_LIST_METADATA,
            ),
        )

    def policy(
        self,
        *,
        include_restrictions: bool | NotGiven = NOT_GIVEN,
        question: str,
        rationale: str,
    ) -> PolicyAnswer:
        """Get an answer to a question about the expense policy or funds (amount, restrictions, etc) (post_agent_tool_api___answer_policy_question)."""
        return cast(
            PolicyAnswer,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/answer-policy-question",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_restrictions": include_restrictions,
                        "question": question,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_POLICY_METADATA,
            ),
        )

    def requirements(
        self,
        *,
        rationale: str,
    ) -> EmployeeSubmissionPolicyRequirementsSuccess:
        """Get the employee-visible expense submission requirements for the caller's business, such as receipt, memo, attendee, fund, and accounting-field requirements per submission policy (get_agent_tool_api___get_employee_submission_policy_requirements)."""
        return cast(
            EmployeeSubmissionPolicyRequirementsSuccess,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-employee-submission-policy-requirements",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_REQUIREMENTS_METADATA,
            ),
        )

    def simulate(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
        workflow_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> SimulatePolicyWorkflowForExpenseSuccess:
        """Simulate an approval or submission policy workflow against an existing transaction or reimbursement to preview how the published policy (or a specific historical workflow version) would route it (post_agent_tool_api___simulate_policy_workflow_for_expense)."""
        return cast(
            SimulatePolicyWorkflowForExpenseSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/simulate-policy-workflow-for-expense",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "kind": kind,
                        "policy_uuid": policy_uuid,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "transaction_uuid": transaction_uuid,
                        "workflow_uuid": workflow_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_SIMULATE_METADATA,
            ),
        )


class AsyncAgentToolsPolicy:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def body(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
        workflow_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetPolicyWorkflowBodyPublicSuccess:
        """Fetch the published (or a specific historical) workflow body for a workflow-backed policy, including compact branch structure, condition operands, and a workflow outline of the visible builder steps (get_agent_tool_api___get_policy_workflow_body)."""
        return cast(
            GetPolicyWorkflowBodyPublicSuccess,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-policy-workflow-body",
                path_params=None,
                params=_without_not_given(
                    {
                        "kind": kind,
                        "policy_uuid": policy_uuid,
                        "rationale": rationale,
                        "workflow_uuid": workflow_uuid,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_BODY_METADATA,
            ),
        )

    async def explain(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> GetExpenseWorkflowContextSuccess:
        """Resolve a transaction or reimbursement UUID to its approval workflow context: the expense summary, its approval chain steps and approvers, the attached approval and submission policies, any travel booking approval, and the latest Policy Agent review (get_agent_tool_api___get_expense_workflow_context)."""
        return cast(
            GetExpenseWorkflowContextSuccess,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-expense-workflow-context",
                path_params=None,
                params=_without_not_given(
                    {
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_EXPLAIN_METADATA,
            ),
        )

    async def get(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
    ) -> PolicyDetailsSuccess:
        """Fetch detailed metadata for one workflow-backed policy by UUID, including display name, spend type, default status, and separation-of-duties configuration (get_agent_tool_api___get_policy_details)."""
        return cast(
            PolicyDetailsSuccess,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-policy-details",
                path_params=None,
                params=_without_not_given(
                    {"kind": kind, "policy_uuid": policy_uuid, "rationale": rationale}
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_GET_METADATA,
            ),
        )

    async def list(
        self,
        *,
        kinds: Sequence[str] | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListPoliciesSuccess:
        """List workflow-backed submission, approval, and spend-request policies for the business, with each policy's UUID, kind, spend type, default status, and workflow availability (get_agent_tool_api___list_policies)."""
        return cast(
            ListPoliciesSuccess,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-policies",
                path_params=None,
                params=_without_not_given({"kinds": kinds, "rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_LIST_METADATA,
            ),
        )

    async def policy(
        self,
        *,
        include_restrictions: bool | NotGiven = NOT_GIVEN,
        question: str,
        rationale: str,
    ) -> PolicyAnswer:
        """Get an answer to a question about the expense policy or funds (amount, restrictions, etc) (post_agent_tool_api___answer_policy_question)."""
        return cast(
            PolicyAnswer,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/answer-policy-question",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_restrictions": include_restrictions,
                        "question": question,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_POLICY_METADATA,
            ),
        )

    async def requirements(
        self,
        *,
        rationale: str,
    ) -> EmployeeSubmissionPolicyRequirementsSuccess:
        """Get the employee-visible expense submission requirements for the caller's business, such as receipt, memo, attendee, fund, and accounting-field requirements per submission policy (get_agent_tool_api___get_employee_submission_policy_requirements)."""
        return cast(
            EmployeeSubmissionPolicyRequirementsSuccess,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-employee-submission-policy-requirements",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_REQUIREMENTS_METADATA,
            ),
        )

    async def simulate(
        self,
        *,
        kind: str,
        policy_uuid: str,
        rationale: str,
        reimbursement_uuid: str | None | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
        workflow_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> SimulatePolicyWorkflowForExpenseSuccess:
        """Simulate an approval or submission policy workflow against an existing transaction or reimbursement to preview how the published policy (or a specific historical workflow version) would route it (post_agent_tool_api___simulate_policy_workflow_for_expense)."""
        return cast(
            SimulatePolicyWorkflowForExpenseSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/simulate-policy-workflow-for-expense",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "kind": kind,
                        "policy_uuid": policy_uuid,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                        "transaction_uuid": transaction_uuid,
                        "workflow_uuid": workflow_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_POLICY_SIMULATE_METADATA,
            ),
        )


class AgentToolsProcurementRequests:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def delete(
        self,
        *,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> DeletedProcurementDraft:
        """Delete an abandoned procurement draft owned by the acting user (delete_agent_tool_api___delete_procurement_draft)."""
        return cast(
            DeletedProcurementDraft,
            self._transport.request(
                method="DELETE",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "spend_request_uuid": spend_request_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_DELETE_METADATA,
            ),
        )

    def draft(
        self,
        *,
        answers: Sequence[Any] | NotGiven = NOT_GIVEN,
        change_request_answers: Sequence[Any] | NotGiven = NOT_GIVEN,
        clear_change_request_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        clear_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        existing_spend_request_uuid: UUID | None | NotGiven = NOT_GIVEN,
        internal_memo: str | None | NotGiven = NOT_GIVEN,
        line_items: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        rationale: str,
        request_name: str | None | NotGiven = NOT_GIVEN,
        request_virtual_card: bool | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: UUID | None | NotGiven = NOT_GIVEN,
        spend_request_uuid: UUID | None | NotGiven = NOT_GIVEN,
    ) -> ProcurementDraftState:
        """Create or update a procurement draft and return the current visible form state (post_agent_tool_api___draft_procurement_request)."""
        return cast(
            ProcurementDraftState,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "answers": answers,
                        "change_request_answers": change_request_answers,
                        "clear_change_request_field_ids": clear_change_request_field_ids,
                        "clear_field_ids": clear_field_ids,
                        "currency": currency,
                        "existing_spend_request_uuid": existing_spend_request_uuid,
                        "internal_memo": internal_memo,
                        "line_items": line_items,
                        "rationale": rationale,
                        "request_name": request_name,
                        "request_virtual_card": request_virtual_card,
                        "spend_intent_uuid": spend_intent_uuid,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_DRAFT_METADATA,
            ),
        )

    def get(
        self,
        *,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementDraftState:
        """Refresh and canonically revalidate a procurement draft's visible form state (get_agent_tool_api___get_procurement_draft)."""
        return cast(
            ProcurementDraftState,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=_without_not_given(
                    {"rationale": rationale, "spend_request_uuid": spend_request_uuid}
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_GET_METADATA,
            ),
        )

    def spend_intents(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        query: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListProcurementSpendIntentsResult:
        """List published procurement spend programs the agent can draft against (post_agent_tool_api___list_procurement_spend_intents)."""
        return cast(
            ListProcurementSpendIntentsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-spend-intents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"page_size": page_size, "query": query, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_SPEND_INTENTS_METADATA,
            ),
        )

    def submit(
        self,
        *,
        confirmed: bool,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementSubmittedRequest:
        """Submit a procurement draft after explicit user confirmation (post_agent_tool_api___submit_procurement_request)."""
        return cast(
            ProcurementSubmittedRequest,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-submit",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirmed": confirmed,
                        "rationale": rationale,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_SUBMIT_METADATA,
            ),
        )

    def upload_file(
        self,
        *,
        field_id: str,
        file: FileInput,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementUploadedFileResultJsonMode:
        """Upload a file for a visible procurement request draft file field (post_agent_tool_api___upload_procurement_file)."""
        return cast(
            ProcurementUploadedFileResultJsonMode,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-upload-file",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=_without_not_given(
                    {
                        "field_id": field_id,
                        "rationale": rationale,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                files=_without_not_given({"file": file}),
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_UPLOAD_FILE_METADATA,
            ),
        )


class AsyncAgentToolsProcurementRequests:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def delete(
        self,
        *,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> DeletedProcurementDraft:
        """Delete an abandoned procurement draft owned by the acting user (delete_agent_tool_api___delete_procurement_draft)."""
        return cast(
            DeletedProcurementDraft,
            await self._transport.request(
                method="DELETE",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "spend_request_uuid": spend_request_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_DELETE_METADATA,
            ),
        )

    async def draft(
        self,
        *,
        answers: Sequence[Any] | NotGiven = NOT_GIVEN,
        change_request_answers: Sequence[Any] | NotGiven = NOT_GIVEN,
        clear_change_request_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        clear_field_ids: Sequence[str] | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        existing_spend_request_uuid: UUID | None | NotGiven = NOT_GIVEN,
        internal_memo: str | None | NotGiven = NOT_GIVEN,
        line_items: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        rationale: str,
        request_name: str | None | NotGiven = NOT_GIVEN,
        request_virtual_card: bool | None | NotGiven = NOT_GIVEN,
        spend_intent_uuid: UUID | None | NotGiven = NOT_GIVEN,
        spend_request_uuid: UUID | None | NotGiven = NOT_GIVEN,
    ) -> ProcurementDraftState:
        """Create or update a procurement draft and return the current visible form state (post_agent_tool_api___draft_procurement_request)."""
        return cast(
            ProcurementDraftState,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "answers": answers,
                        "change_request_answers": change_request_answers,
                        "clear_change_request_field_ids": clear_change_request_field_ids,
                        "clear_field_ids": clear_field_ids,
                        "currency": currency,
                        "existing_spend_request_uuid": existing_spend_request_uuid,
                        "internal_memo": internal_memo,
                        "line_items": line_items,
                        "rationale": rationale,
                        "request_name": request_name,
                        "request_virtual_card": request_virtual_card,
                        "spend_intent_uuid": spend_intent_uuid,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_DRAFT_METADATA,
            ),
        )

    async def get(
        self,
        *,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementDraftState:
        """Refresh and canonically revalidate a procurement draft's visible form state (get_agent_tool_api___get_procurement_draft)."""
        return cast(
            ProcurementDraftState,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/procurement-draft",
                path_params=None,
                params=_without_not_given(
                    {"rationale": rationale, "spend_request_uuid": spend_request_uuid}
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_GET_METADATA,
            ),
        )

    async def spend_intents(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        query: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListProcurementSpendIntentsResult:
        """List published procurement spend programs the agent can draft against (post_agent_tool_api___list_procurement_spend_intents)."""
        return cast(
            ListProcurementSpendIntentsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-spend-intents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"page_size": page_size, "query": query, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_SPEND_INTENTS_METADATA,
            ),
        )

    async def submit(
        self,
        *,
        confirmed: bool,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementSubmittedRequest:
        """Submit a procurement draft after explicit user confirmation (post_agent_tool_api___submit_procurement_request)."""
        return cast(
            ProcurementSubmittedRequest,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-submit",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirmed": confirmed,
                        "rationale": rationale,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_SUBMIT_METADATA,
            ),
        )

    async def upload_file(
        self,
        *,
        field_id: str,
        file: FileInput,
        rationale: str,
        spend_request_uuid: UUID,
    ) -> ProcurementUploadedFileResultJsonMode:
        """Upload a file for a visible procurement request draft file field (post_agent_tool_api___upload_procurement_file)."""
        return cast(
            ProcurementUploadedFileResultJsonMode,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/procurement-upload-file",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=_without_not_given(
                    {
                        "field_id": field_id,
                        "rationale": rationale,
                        "spend_request_uuid": spend_request_uuid,
                    }
                ),
                files=_without_not_given({"file": file}),
                metadata=_AGENT_TOOLS_PROCUREMENT_REQUESTS_UPLOAD_FILE_METADATA,
            ),
        )


class AgentToolsPurchaseOrders:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(
        self,
        *,
        purchase_order_id: UUID,
        rationale: str,
    ) -> PurchaseOrderDetails:
        """Get comprehensive details about a specific purchase order (post_agent_tool_api___get_purchase_order_details)."""
        return cast(
            PurchaseOrderDetails,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-purchase-order-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"purchase_order_id": purchase_order_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_GET_METADATA,
            ),
        )

    def ramp_bulk_close_purchase_orders(
        self,
        *,
        close_reason: str,
        purchase_order_uuids: Sequence[str],
        rationale: str,
    ) -> BulkClosePurchaseOrdersResult:
        """Close one or more purchase orders with a specified reason (post_agent_tool_api___bulk_close_purchase_orders)."""
        return cast(
            BulkClosePurchaseOrdersResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/ramp_bulk_close_purchase_orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_reason": close_reason,
                        "purchase_order_uuids": purchase_order_uuids,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_CLOSE_PURCHASE_ORDERS_METADATA,
            ),
        )

    def ramp_bulk_reopen_purchase_orders(
        self,
        *,
        purchase_order_uuids: Sequence[str],
        rationale: str,
    ) -> BulkReopenPurchaseOrdersResult:
        """Reopen multiple closed purchase orders (post_agent_tool_api___bulk_reopen_purchase_orders)."""
        return cast(
            BulkReopenPurchaseOrdersResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/ramp_bulk_reopen_purchase_orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "purchase_order_uuids": purchase_order_uuids,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_REOPEN_PURCHASE_ORDERS_METADATA,
            ),
        )

    def search(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PurchaseOrderSearchResult:
        """Search for purchase orders using structured purchase order filters (post_agent_tool_api___search_purchase_orders)."""
        return cast(
            PurchaseOrderSearchResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-purchase-orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_SEARCH_METADATA,
            ),
        )


class AsyncAgentToolsPurchaseOrders:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(
        self,
        *,
        purchase_order_id: UUID,
        rationale: str,
    ) -> PurchaseOrderDetails:
        """Get comprehensive details about a specific purchase order (post_agent_tool_api___get_purchase_order_details)."""
        return cast(
            PurchaseOrderDetails,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-purchase-order-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"purchase_order_id": purchase_order_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_GET_METADATA,
            ),
        )

    async def ramp_bulk_close_purchase_orders(
        self,
        *,
        close_reason: str,
        purchase_order_uuids: Sequence[str],
        rationale: str,
    ) -> BulkClosePurchaseOrdersResult:
        """Close one or more purchase orders with a specified reason (post_agent_tool_api___bulk_close_purchase_orders)."""
        return cast(
            BulkClosePurchaseOrdersResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/ramp_bulk_close_purchase_orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_reason": close_reason,
                        "purchase_order_uuids": purchase_order_uuids,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_CLOSE_PURCHASE_ORDERS_METADATA,
            ),
        )

    async def ramp_bulk_reopen_purchase_orders(
        self,
        *,
        purchase_order_uuids: Sequence[str],
        rationale: str,
    ) -> BulkReopenPurchaseOrdersResult:
        """Reopen multiple closed purchase orders (post_agent_tool_api___bulk_reopen_purchase_orders)."""
        return cast(
            BulkReopenPurchaseOrdersResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/ramp_bulk_reopen_purchase_orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "purchase_order_uuids": purchase_order_uuids,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_RAMP_BULK_REOPEN_PURCHASE_ORDERS_METADATA,
            ),
        )

    async def search(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> PurchaseOrderSearchResult:
        """Search for purchase orders using structured purchase order filters (post_agent_tool_api___search_purchase_orders)."""
        return cast(
            PurchaseOrderSearchResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-purchase-orders",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_PURCHASE_ORDERS_SEARCH_METADATA,
            ),
        )


class AgentToolsReceipts:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach(
        self,
        *,
        rationale: str,
        receipt_uuid: str,
        transaction_uuid: str,
    ) -> AttachReceiptSuccess:
        """Attach an existing receipt to a transaction (post_agent_tool_api___attach_receipt_to_transaction)."""
        return cast(
            AttachReceiptSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/attach-receipt-to-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "receipt_uuid": receipt_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RECEIPTS_ATTACH_METADATA,
            ),
        )

    def upload(
        self,
        *,
        content_type: str,
        file_content_base64: str,
        filename: str,
        rationale: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> ReceiptUploadSuccess:
        """Upload a receipt from base64-encoded file content (post_agent_tool_api___upload_receipt_file)."""
        return cast(
            ReceiptUploadSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/upload-receipt-file",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "content_type": content_type,
                        "file_content_base64": file_content_base64,
                        "filename": filename,
                        "rationale": rationale,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RECEIPTS_UPLOAD_METADATA,
            ),
        )


class AsyncAgentToolsReceipts:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach(
        self,
        *,
        rationale: str,
        receipt_uuid: str,
        transaction_uuid: str,
    ) -> AttachReceiptSuccess:
        """Attach an existing receipt to a transaction (post_agent_tool_api___attach_receipt_to_transaction)."""
        return cast(
            AttachReceiptSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/attach-receipt-to-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "receipt_uuid": receipt_uuid,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RECEIPTS_ATTACH_METADATA,
            ),
        )

    async def upload(
        self,
        *,
        content_type: str,
        file_content_base64: str,
        filename: str,
        rationale: str,
        transaction_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> ReceiptUploadSuccess:
        """Upload a receipt from base64-encoded file content (post_agent_tool_api___upload_receipt_file)."""
        return cast(
            ReceiptUploadSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/upload-receipt-file",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "content_type": content_type,
                        "file_content_base64": file_content_base64,
                        "filename": filename,
                        "rationale": rationale,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RECEIPTS_UPLOAD_METADATA,
            ),
        )


class AgentToolsReimbursements:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def approve(
        self,
        *,
        action: str,
        rationale: str,
        reimbursement_id: str,
        thoughts: str | None | NotGiven = NOT_GIVEN,
        user_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> ReimbursementActionResult:
        """Approve or reject an employee reimbursement request for an out-of-pocket expense (post_agent_tool_api___approve_or_reject_reimbursement)."""
        return cast(
            ReimbursementActionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "reimbursement_id": reimbursement_id,
                        "thoughts": thoughts,
                        "user_reason": user_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_APPROVE_METADATA,
            ),
        )

    def cancel(
        self,
        *,
        notes: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> CancelReimbursementPaymentSuccess:
        """Cancel the payment on a reimbursement that has been approved but not yet paid out (post_agent_tool_api___cancel_reimbursement_payment)."""
        return cast(
            CancelReimbursementPaymentSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/cancel-reimbursement-payment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "notes": notes,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_CANCEL_METADATA,
            ),
        )

    def create(
        self,
        *,
        amount: Any | None | NotGiven = NOT_GIVEN,
        currency_code: str | None | NotGiven = NOT_GIVEN,
        merchant: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        receipt_uuid: str,
        transaction_date: str | None | NotGiven = NOT_GIVEN,
    ) -> ReimbursementCreationSuccess:
        """Create a draft reimbursement from a receipt UUID (post_agent_tool_api___create_reimbursement_from_receipt)."""
        return cast(
            ReimbursementCreationSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-reimbursement-from-receipt",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency_code": currency_code,
                        "merchant": merchant,
                        "rationale": rationale,
                        "receipt_uuid": receipt_uuid,
                        "transaction_date": transaction_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_CREATE_METADATA,
            ),
        )

    def delete(
        self,
        *,
        rationale: str,
        reimbursement_uuid: UUID | None,
    ) -> DeleteReimbursementSuccess:
        """Delete a reimbursement by UUID (post_agent_tool_api___delete_reimbursement)."""
        return cast(
            DeleteReimbursementSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/delete-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_DELETE_METADATA,
            ),
        )

    def duplicate(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> DuplicateReimbursementSuccess:
        """Duplicate an existing reimbursement as a new draft (post_agent_tool_api___duplicate_reimbursement)."""
        return cast(
            DuplicateReimbursementSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/duplicate-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_DUPLICATE_METADATA,
            ),
        )

    def edit(
        self,
        *,
        accounting_split_request: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        amount: Any | None | NotGiven = NOT_GIVEN,
        attendee_user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        currency_code: str | None | NotGiven = NOT_GIVEN,
        custom_record_values: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        memo: str | None | NotGiven = NOT_GIVEN,
        merchant_name: str | None | NotGiven = NOT_GIVEN,
        merchant_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_date: str | None | NotGiven = NOT_GIVEN,
        reimbursement_uuid: str | None,
        tracking_category_selections: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        trip_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> EditReimbursementSuccess:
        """Edit reimbursement fields (amount, currency, date, merchant, memo, funds, accounting categories, split line items, custom records, trip, attendees) (post_agent_tool_api___edit_reimbursement)."""
        return cast(
            EditReimbursementSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accounting_split_request": accounting_split_request,
                        "amount": amount,
                        "attendee_user_uuids": attendee_user_uuids,
                        "currency_code": currency_code,
                        "custom_record_values": custom_record_values,
                        "fund_uuid": fund_uuid,
                        "memo": memo,
                        "merchant_name": merchant_name,
                        "merchant_uuid": merchant_uuid,
                        "rationale": rationale,
                        "reimbursement_date": reimbursement_date,
                        "reimbursement_uuid": reimbursement_uuid,
                        "tracking_category_selections": tracking_category_selections,
                        "trip_uuid": trip_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_EDIT_METADATA,
            ),
        )

    def estimate(
        self,
        *,
        distance: Any,
        distance_units: str | NotGiven = NOT_GIVEN,
        rationale: str,
        transaction_date: str | None | NotGiven = NOT_GIVEN,
        vehicle_mileage_class: str | None | NotGiven = NOT_GIVEN,
    ) -> EstimateMileageReimbursementResult:
        """Estimate the reimbursement amount for a given mileage distance based on the user's company rates (post_agent_tool_api___estimate_mileage_reimbursement)."""
        return cast(
            EstimateMileageReimbursementResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/estimate-mileage-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "distance": distance,
                        "distance_units": distance_units,
                        "rationale": rationale,
                        "transaction_date": transaction_date,
                        "vehicle_mileage_class": vehicle_mileage_class,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_METADATA,
            ),
        )

    def estimate_per_diem_amount(
        self,
        *,
        day_data: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        deduct_weekends: bool | None | NotGiven = NOT_GIVEN,
        end_date: str,
        meals_provided: bool | None | NotGiven = NOT_GIVEN,
        rationale: str,
        start_date: str,
        trip_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> EstimatePerDiemAmountSuccess:
        """Estimate the per diem reimbursement amount for a trip given start/end dates and optional meal deductions (post_agent_tool_api___estimate_per_diem_amount)."""
        return cast(
            EstimatePerDiemAmountSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/estimate-per-diem-amount",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "day_data": day_data,
                        "deduct_weekends": deduct_weekends,
                        "end_date": end_date,
                        "meals_provided": meals_provided,
                        "rationale": rationale,
                        "start_date": start_date,
                        "trip_uuid": trip_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_PER_DIEM_AMOUNT_METADATA,
            ),
        )

    def list(
        self,
        *,
        from_date: str | None | NotGiven = NOT_GIVEN,
        include_policy_assessment: bool | NotGiven = NOT_GIVEN,
        include_suggestions: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        reimbursements_to_retrieve: str | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        tags: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> GetReimbursementsResult:
        """Search and retrieve reimbursements with filters for users, text search, (post_agent_tool_api___get_reimbursements)."""
        return cast(
            GetReimbursementsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "from_date": from_date,
                        "include_policy_assessment": include_policy_assessment,
                        "include_suggestions": include_suggestions,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_uuids": reimbursement_uuids,
                        "reimbursements_to_retrieve": reimbursements_to_retrieve,
                        "search_string": search_string,
                        "tags": tags,
                        "to_date": to_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_LIST_METADATA,
            ),
        )

    def outstanding(
        self,
        *,
        entity_uuid: str | None | NotGiven = NOT_GIVEN,
        new_currency: str,
        rationale: str,
    ) -> GetOutstandingReimbursementsSuccess:
        """Get approved and failed reimbursements that would be affected by a bank account currency change (post_agent_tool_api___get_outstanding_reimbursements_by_currency)."""
        return cast(
            GetOutstandingReimbursementsSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-outstanding-reimbursements-by-currency",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "entity_uuid": entity_uuid,
                        "new_currency": new_currency,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_OUTSTANDING_METADATA,
            ),
        )

    def pending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ReimbursementsForApproval:
        """Get employee reimbursements pending approval by the current user (post_agent_tool_api___get_reimbursements_for_approval)."""
        return cast(
            ReimbursementsForApproval,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursements-for-approval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"limit": limit, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_PENDING_METADATA,
            ),
        )

    def receipts(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> GetReimbursementReceiptsSuccess:
        """Retrieve receipts attached to a reimbursement (post_agent_tool_api___get_reimbursement_receipts)."""
        return cast(
            GetReimbursementReceiptsSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursement-receipts",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RECEIPTS_METADATA,
            ),
        )

    def recent(
        self,
        *,
        include_drafts: bool | NotGiven = NOT_GIVEN,
        include_rejected: bool | NotGiven = NOT_GIVEN,
        limit: int | None | NotGiven = NOT_GIVEN,
        rationale: str,
        up_to_days: int | NotGiven = NOT_GIVEN,
        use_submitted_date_ordering: bool | NotGiven = NOT_GIVEN,
    ) -> RecentReimbursements:
        """Get reimbursement history for the current user (post_agent_tool_api___get_user_recent_reimbursements)."""
        return cast(
            RecentReimbursements,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-user-recent-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_drafts": include_drafts,
                        "include_rejected": include_rejected,
                        "limit": limit,
                        "rationale": rationale,
                        "up_to_days": up_to_days,
                        "use_submitted_date_ordering": use_submitted_date_ordering,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RECENT_METADATA,
            ),
        )

    def resubmit(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> ResubmitReimbursementSuccess:
        """Revert a rejected reimbursement back to draft state so it can be edited and resubmitted (post_agent_tool_api___resubmit_reimbursement)."""
        return cast(
            ResubmitReimbursementSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/resubmit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RESUBMIT_METADATA,
            ),
        )

    def search(
        self,
        *,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_status: str | None | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> SearchReimbursementsResult:
        """Search reimbursements with text-based filters and structured filters (post_agent_tool_api___search_user_reimbursements)."""
        return cast(
            SearchReimbursementsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-user-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "from_date": from_date,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_status": reimbursement_status,
                        "search_string": search_string,
                        "to_date": to_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_METADATA,
            ),
        )

    def search_reimbursements(
        self,
        *,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_status: str | None | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
        user_id: int | None | NotGiven = NOT_GIVEN,
    ) -> SearchReimbursementsResult:
        """Search reimbursements across a business, optionally filtering to a specific user's reimbursements (post_agent_tool_api___search_reimbursements)."""
        return cast(
            SearchReimbursementsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "from_date": from_date,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_status": reimbursement_status,
                        "search_string": search_string,
                        "to_date": to_date,
                        "user_id": user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_REIMBURSEMENTS_METADATA,
            ),
        )

    def submit(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> SubmitReimbursementSuccess:
        """Submit a draft out-of-pocket reimbursement for approval (post_agent_tool_api___submit_reimbursement)."""
        return cast(
            SubmitReimbursementSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SUBMIT_METADATA,
            ),
        )


class AsyncAgentToolsReimbursements:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def approve(
        self,
        *,
        action: str,
        rationale: str,
        reimbursement_id: str,
        thoughts: str | None | NotGiven = NOT_GIVEN,
        user_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> ReimbursementActionResult:
        """Approve or reject an employee reimbursement request for an out-of-pocket expense (post_agent_tool_api___approve_or_reject_reimbursement)."""
        return cast(
            ReimbursementActionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "reimbursement_id": reimbursement_id,
                        "thoughts": thoughts,
                        "user_reason": user_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_APPROVE_METADATA,
            ),
        )

    async def cancel(
        self,
        *,
        notes: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> CancelReimbursementPaymentSuccess:
        """Cancel the payment on a reimbursement that has been approved but not yet paid out (post_agent_tool_api___cancel_reimbursement_payment)."""
        return cast(
            CancelReimbursementPaymentSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/cancel-reimbursement-payment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "notes": notes,
                        "rationale": rationale,
                        "reimbursement_uuid": reimbursement_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_CANCEL_METADATA,
            ),
        )

    async def create(
        self,
        *,
        amount: Any | None | NotGiven = NOT_GIVEN,
        currency_code: str | None | NotGiven = NOT_GIVEN,
        merchant: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        receipt_uuid: str,
        transaction_date: str | None | NotGiven = NOT_GIVEN,
    ) -> ReimbursementCreationSuccess:
        """Create a draft reimbursement from a receipt UUID (post_agent_tool_api___create_reimbursement_from_receipt)."""
        return cast(
            ReimbursementCreationSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-reimbursement-from-receipt",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "currency_code": currency_code,
                        "merchant": merchant,
                        "rationale": rationale,
                        "receipt_uuid": receipt_uuid,
                        "transaction_date": transaction_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_CREATE_METADATA,
            ),
        )

    async def delete(
        self,
        *,
        rationale: str,
        reimbursement_uuid: UUID | None,
    ) -> DeleteReimbursementSuccess:
        """Delete a reimbursement by UUID (post_agent_tool_api___delete_reimbursement)."""
        return cast(
            DeleteReimbursementSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/delete-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_DELETE_METADATA,
            ),
        )

    async def duplicate(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> DuplicateReimbursementSuccess:
        """Duplicate an existing reimbursement as a new draft (post_agent_tool_api___duplicate_reimbursement)."""
        return cast(
            DuplicateReimbursementSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/duplicate-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_DUPLICATE_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        accounting_split_request: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        amount: Any | None | NotGiven = NOT_GIVEN,
        attendee_user_uuids: Sequence[str] | NotGiven = NOT_GIVEN,
        currency_code: str | None | NotGiven = NOT_GIVEN,
        custom_record_values: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        memo: str | None | NotGiven = NOT_GIVEN,
        merchant_name: str | None | NotGiven = NOT_GIVEN,
        merchant_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_date: str | None | NotGiven = NOT_GIVEN,
        reimbursement_uuid: str | None,
        tracking_category_selections: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        trip_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> EditReimbursementSuccess:
        """Edit reimbursement fields (amount, currency, date, merchant, memo, funds, accounting categories, split line items, custom records, trip, attendees) (post_agent_tool_api___edit_reimbursement)."""
        return cast(
            EditReimbursementSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accounting_split_request": accounting_split_request,
                        "amount": amount,
                        "attendee_user_uuids": attendee_user_uuids,
                        "currency_code": currency_code,
                        "custom_record_values": custom_record_values,
                        "fund_uuid": fund_uuid,
                        "memo": memo,
                        "merchant_name": merchant_name,
                        "merchant_uuid": merchant_uuid,
                        "rationale": rationale,
                        "reimbursement_date": reimbursement_date,
                        "reimbursement_uuid": reimbursement_uuid,
                        "tracking_category_selections": tracking_category_selections,
                        "trip_uuid": trip_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_EDIT_METADATA,
            ),
        )

    async def estimate(
        self,
        *,
        distance: Any,
        distance_units: str | NotGiven = NOT_GIVEN,
        rationale: str,
        transaction_date: str | None | NotGiven = NOT_GIVEN,
        vehicle_mileage_class: str | None | NotGiven = NOT_GIVEN,
    ) -> EstimateMileageReimbursementResult:
        """Estimate the reimbursement amount for a given mileage distance based on the user's company rates (post_agent_tool_api___estimate_mileage_reimbursement)."""
        return cast(
            EstimateMileageReimbursementResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/estimate-mileage-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "distance": distance,
                        "distance_units": distance_units,
                        "rationale": rationale,
                        "transaction_date": transaction_date,
                        "vehicle_mileage_class": vehicle_mileage_class,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_METADATA,
            ),
        )

    async def estimate_per_diem_amount(
        self,
        *,
        day_data: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        deduct_weekends: bool | None | NotGiven = NOT_GIVEN,
        end_date: str,
        meals_provided: bool | None | NotGiven = NOT_GIVEN,
        rationale: str,
        start_date: str,
        trip_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> EstimatePerDiemAmountSuccess:
        """Estimate the per diem reimbursement amount for a trip given start/end dates and optional meal deductions (post_agent_tool_api___estimate_per_diem_amount)."""
        return cast(
            EstimatePerDiemAmountSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/estimate-per-diem-amount",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "day_data": day_data,
                        "deduct_weekends": deduct_weekends,
                        "end_date": end_date,
                        "meals_provided": meals_provided,
                        "rationale": rationale,
                        "start_date": start_date,
                        "trip_uuid": trip_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_ESTIMATE_PER_DIEM_AMOUNT_METADATA,
            ),
        )

    async def list(
        self,
        *,
        from_date: str | None | NotGiven = NOT_GIVEN,
        include_policy_assessment: bool | NotGiven = NOT_GIVEN,
        include_suggestions: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_uuids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        reimbursements_to_retrieve: str | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        tags: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> GetReimbursementsResult:
        """Search and retrieve reimbursements with filters for users, text search, (post_agent_tool_api___get_reimbursements)."""
        return cast(
            GetReimbursementsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "from_date": from_date,
                        "include_policy_assessment": include_policy_assessment,
                        "include_suggestions": include_suggestions,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_uuids": reimbursement_uuids,
                        "reimbursements_to_retrieve": reimbursements_to_retrieve,
                        "search_string": search_string,
                        "tags": tags,
                        "to_date": to_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_LIST_METADATA,
            ),
        )

    async def outstanding(
        self,
        *,
        entity_uuid: str | None | NotGiven = NOT_GIVEN,
        new_currency: str,
        rationale: str,
    ) -> GetOutstandingReimbursementsSuccess:
        """Get approved and failed reimbursements that would be affected by a bank account currency change (post_agent_tool_api___get_outstanding_reimbursements_by_currency)."""
        return cast(
            GetOutstandingReimbursementsSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-outstanding-reimbursements-by-currency",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "entity_uuid": entity_uuid,
                        "new_currency": new_currency,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_OUTSTANDING_METADATA,
            ),
        )

    async def pending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ReimbursementsForApproval:
        """Get employee reimbursements pending approval by the current user (post_agent_tool_api___get_reimbursements_for_approval)."""
        return cast(
            ReimbursementsForApproval,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursements-for-approval",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"limit": limit, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_PENDING_METADATA,
            ),
        )

    async def receipts(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> GetReimbursementReceiptsSuccess:
        """Retrieve receipts attached to a reimbursement (post_agent_tool_api___get_reimbursement_receipts)."""
        return cast(
            GetReimbursementReceiptsSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-reimbursement-receipts",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RECEIPTS_METADATA,
            ),
        )

    async def recent(
        self,
        *,
        include_drafts: bool | NotGiven = NOT_GIVEN,
        include_rejected: bool | NotGiven = NOT_GIVEN,
        limit: int | None | NotGiven = NOT_GIVEN,
        rationale: str,
        up_to_days: int | NotGiven = NOT_GIVEN,
        use_submitted_date_ordering: bool | NotGiven = NOT_GIVEN,
    ) -> RecentReimbursements:
        """Get reimbursement history for the current user (post_agent_tool_api___get_user_recent_reimbursements)."""
        return cast(
            RecentReimbursements,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-user-recent-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_drafts": include_drafts,
                        "include_rejected": include_rejected,
                        "limit": limit,
                        "rationale": rationale,
                        "up_to_days": up_to_days,
                        "use_submitted_date_ordering": use_submitted_date_ordering,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RECENT_METADATA,
            ),
        )

    async def resubmit(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> ResubmitReimbursementSuccess:
        """Revert a rejected reimbursement back to draft state so it can be edited and resubmitted (post_agent_tool_api___resubmit_reimbursement)."""
        return cast(
            ResubmitReimbursementSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/resubmit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_RESUBMIT_METADATA,
            ),
        )

    async def search(
        self,
        *,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_status: str | None | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> SearchReimbursementsResult:
        """Search reimbursements with text-based filters and structured filters (post_agent_tool_api___search_user_reimbursements)."""
        return cast(
            SearchReimbursementsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-user-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "from_date": from_date,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_status": reimbursement_status,
                        "search_string": search_string,
                        "to_date": to_date,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_METADATA,
            ),
        )

    async def search_reimbursements(
        self,
        *,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reimbursement_status: str | None | NotGiven = NOT_GIVEN,
        search_string: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
        user_id: int | None | NotGiven = NOT_GIVEN,
    ) -> SearchReimbursementsResult:
        """Search reimbursements across a business, optionally filtering to a specific user's reimbursements (post_agent_tool_api___search_reimbursements)."""
        return cast(
            SearchReimbursementsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-reimbursements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "from_date": from_date,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reimbursement_status": reimbursement_status,
                        "search_string": search_string,
                        "to_date": to_date,
                        "user_id": user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SEARCH_REIMBURSEMENTS_METADATA,
            ),
        )

    async def submit(
        self,
        *,
        rationale: str,
        reimbursement_uuid: str | None,
    ) -> SubmitReimbursementSuccess:
        """Submit a draft out-of-pocket reimbursement for approval (post_agent_tool_api___submit_reimbursement)."""
        return cast(
            SubmitReimbursementSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-reimbursement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "reimbursement_uuid": reimbursement_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REIMBURSEMENTS_SUBMIT_METADATA,
            ),
        )


class AgentToolsRequests:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def approve(
        self,
        *,
        action: str,
        rationale: str,
        thoughts: str,
        unified_request_id: str | None,
    ) -> UnifiedRequestActionResult:
        """Approve or reject a pending unified request for spend allocation (fund), purchase order, or procurement approval (post_agent_tool_api___approve_or_reject_request)."""
        return cast(
            UnifiedRequestActionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-request",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "thoughts": thoughts,
                        "unified_request_id": unified_request_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_APPROVE_METADATA,
            ),
        )

    def get(
        self,
        *,
        rationale: str,
        unified_request_id: str,
    ) -> UnifiedRequestDetailsOutput:
        """Get detailed information about a specific unified request the acting user can view (post_agent_tool_api___get_unified_request_details)."""
        return cast(
            UnifiedRequestDetailsOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-unified-request-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "unified_request_id": unified_request_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_GET_METADATA,
            ),
        )

    def pending(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        request_types: Sequence[str] | NotGiven = NOT_GIVEN,
        start: str | None | NotGiven = NOT_GIVEN,
        thoughts: str,
    ) -> UnifiedRequestListResult:
        """Get requests that require the current user's review and approval (post_agent_tool_api___get_requests_to_review)."""
        return cast(
            UnifiedRequestListResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-requests-to-review",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "page_size": page_size,
                        "rationale": rationale,
                        "request_types": request_types,
                        "start": start,
                        "thoughts": thoughts,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_PENDING_METADATA,
            ),
        )

    def search(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> UnifiedRequestListResult:
        """Search for unified requests using free-text and structured request filters (post_agent_tool_api___search_unified_requests)."""
        return cast(
            UnifiedRequestListResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-unified-requests",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_SEARCH_METADATA,
            ),
        )


class AsyncAgentToolsRequests:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def approve(
        self,
        *,
        action: str,
        rationale: str,
        thoughts: str,
        unified_request_id: str | None,
    ) -> UnifiedRequestActionResult:
        """Approve or reject a pending unified request for spend allocation (fund), purchase order, or procurement approval (post_agent_tool_api___approve_or_reject_request)."""
        return cast(
            UnifiedRequestActionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-request",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "thoughts": thoughts,
                        "unified_request_id": unified_request_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_APPROVE_METADATA,
            ),
        )

    async def get(
        self,
        *,
        rationale: str,
        unified_request_id: str,
    ) -> UnifiedRequestDetailsOutput:
        """Get detailed information about a specific unified request the acting user can view (post_agent_tool_api___get_unified_request_details)."""
        return cast(
            UnifiedRequestDetailsOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-unified-request-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "unified_request_id": unified_request_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_GET_METADATA,
            ),
        )

    async def pending(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        request_types: Sequence[str] | NotGiven = NOT_GIVEN,
        start: str | None | NotGiven = NOT_GIVEN,
        thoughts: str,
    ) -> UnifiedRequestListResult:
        """Get requests that require the current user's review and approval (post_agent_tool_api___get_requests_to_review)."""
        return cast(
            UnifiedRequestListResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-requests-to-review",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "page_size": page_size,
                        "rationale": rationale,
                        "request_types": request_types,
                        "start": start,
                        "thoughts": thoughts,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_PENDING_METADATA,
            ),
        )

    async def search(
        self,
        *,
        filters: dict[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> UnifiedRequestListResult:
        """Search for unified requests using free-text and structured request filters (post_agent_tool_api___search_unified_requests)."""
        return cast(
            UnifiedRequestListResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-unified-requests",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "filters": filters,
                        "limit": limit,
                        "page_cursor": page_cursor,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_REQUESTS_SEARCH_METADATA,
            ),
        )


class AgentToolsResearch:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def help_center(
        self,
        *,
        query: str,
        query_variants: Any | None | NotGiven = NOT_GIVEN,
        rationale: str,
        top_k: int | NotGiven = NOT_GIVEN,
    ) -> SearchHelpCenterOutput:
        """Tool for searching Ramp's help center documentation using RAG (Retrieval Augmented Generation) (post_agent_tool_api___search_help_center_snippets)."""
        return cast(
            SearchHelpCenterOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-help-center-snippets",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "query": query,
                        "query_variants": query_variants,
                        "rationale": rationale,
                        "top_k": top_k,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RESEARCH_HELP_CENTER_METADATA,
            ),
        )


class AsyncAgentToolsResearch:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def help_center(
        self,
        *,
        query: str,
        query_variants: Any | None | NotGiven = NOT_GIVEN,
        rationale: str,
        top_k: int | NotGiven = NOT_GIVEN,
    ) -> SearchHelpCenterOutput:
        """Tool for searching Ramp's help center documentation using RAG (Retrieval Augmented Generation) (post_agent_tool_api___search_help_center_snippets)."""
        return cast(
            SearchHelpCenterOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-help-center-snippets",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "query": query,
                        "query_variants": query_variants,
                        "rationale": rationale,
                        "top_k": top_k,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_RESEARCH_HELP_CENTER_METADATA,
            ),
        )


class AgentToolsSourcing:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def award(
        self,
        *,
        payee_uuid: UUID,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> AwardSourcingEventOutput:
        """Award the winning vendor for a sourcing event, deciding the event and (post_agent_tool_api___award_sourcing_event)."""
        return cast(
            AwardSourcingEventOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/award-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "sourcing_event_id": sourcing_event_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_AWARD_METADATA,
            ),
        )

    def close_event(
        self,
        *,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> CloseSourcingEventOutput:
        """Close (archive) a sourcing event without awarding a vendor (post_agent_tool_api___close_sourcing_event)."""
        return cast(
            CloseSourcingEventOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/close-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sourcing_event_id": sourcing_event_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_CLOSE_EVENT_METADATA,
            ),
        )

    def collaborators(
        self,
        *,
        add_user_uuids: Sequence[UUID] | NotGiven = NOT_GIVEN,
        rationale: str,
        remove_user_uuids: Sequence[UUID] | NotGiven = NOT_GIVEN,
        rfx_id: UUID,
    ) -> ManageRFXCollaboratorsOutput:
        """Add and/or remove collaborators on an existing RFX (RFI, RFP, or RFQ) (post_agent_tool_api___manage_rfx_collaborators)."""
        return cast(
            ManageRFXCollaboratorsOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/manage-rfx-collaborators",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "add_user_uuids": add_user_uuids,
                        "rationale": rationale,
                        "remove_user_uuids": remove_user_uuids,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_COLLABORATORS_METADATA,
            ),
        )

    def cover_sheet(
        self,
        *,
        attachment_ramp_document_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        body_markdown: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID,
    ) -> SetRFXCoverSheetOutput:
        """Set or update the vendor-facing cover sheet on a DRAFT RFX (post_agent_tool_api___set_rfx_cover_sheet)."""
        return cast(
            SetRFXCoverSheetOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-cover-sheet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attachment_ramp_document_ids": attachment_ramp_document_ids,
                        "body_markdown": body_markdown,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_COVER_SHEET_METADATA,
            ),
        )

    def create(
        self,
        *,
        close_date: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        response_submission_deadline: str | None | NotGiven = NOT_GIVEN,
        rfx_type: str | NotGiven = NOT_GIVEN,
        sections: Sequence[dict[str, Any]],
        sourcing_event_id: UUID | None | NotGiven = NOT_GIVEN,
        sourcing_event_name: str | None | NotGiven = NOT_GIVEN,
    ) -> CreateRFXOutput:
        """Create a DRAFT RFX questionnaire, optionally creating its parent sourcing (post_agent_tool_api___create_rfx)."""
        return cast(
            CreateRFXOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_date": close_date,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "response_submission_deadline": response_submission_deadline,
                        "rfx_type": rfx_type,
                        "sections": sections,
                        "sourcing_event_id": sourcing_event_id,
                        "sourcing_event_name": sourcing_event_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_CREATE_METADATA,
            ),
        )

    def draft_spend_request(
        self,
        *,
        payee_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID | None | NotGiven = NOT_GIVEN,
        sourcing_event_id: UUID,
        spend_intent_uuid: UUID | None | NotGiven = NOT_GIVEN,
    ) -> CreateDraftSpendRequestFromSourcingEventOutput:
        """Hand off an awarded sourcing event into procurement intake by drafting a (post_agent_tool_api___create_draft_spend_request_from_sourcing_event)."""
        return cast(
            CreateDraftSpendRequestFromSourcingEventOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-draft-spend-request-from-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                        "sourcing_event_id": sourcing_event_id,
                        "spend_intent_uuid": spend_intent_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_DRAFT_SPEND_REQUEST_METADATA,
            ),
        )

    def edit(
        self,
        *,
        close_date: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        response_submission_deadline: str | None | NotGiven = NOT_GIVEN,
        rfx_id: UUID,
        sections: Sequence[dict[str, Any]],
    ) -> UpdateRFXOutput:
        """Update an RFX's name, description, dates, and questionnaire sections (post_agent_tool_api___update_rfx)."""
        return cast(
            UpdateRFXOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_date": close_date,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "response_submission_deadline": response_submission_deadline,
                        "rfx_id": rfx_id,
                        "sections": sections,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_EDIT_METADATA,
            ),
        )

    def event(
        self,
        *,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> GetSourcingEventContextOutput:
        """Get a compact summary of a sourcing event, its RFXs, and invited vendors (post_agent_tool_api___get_sourcing_event_context)."""
        return cast(
            GetSourcingEventContextOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-sourcing-event-context",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sourcing_event_id": sourcing_event_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_EVENT_METADATA,
            ),
        )

    def grading(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXGradingOverviewOutput:
        """Get grading outcomes for an RFX: AI-generated grading insights and (post_agent_tool_api___get_rfx_grading_overview)."""
        return cast(
            GetRFXGradingOverviewOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-grading-overview",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_GRADING_METADATA,
            ),
        )

    def invitation_contact(
        self,
        *,
        payee_contact_id: UUID,
        rationale: str,
        rfx_vendor_invitation_id: UUID,
    ) -> SetRFXVendorInvitationContactOutput:
        """Set or replace the contact on an RFX vendor invitation (post_agent_tool_api___set_rfx_vendor_invitation_contact)."""
        return cast(
            SetRFXVendorInvitationContactOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-vendor-invitation-contact",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_contact_id": payee_contact_id,
                        "rationale": rationale,
                        "rfx_vendor_invitation_id": rfx_vendor_invitation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_INVITATION_CONTACT_METADATA,
            ),
        )

    def invite(
        self,
        *,
        rationale: str,
        rfx_id: str,
        vendors: Sequence[dict[str, Any]],
    ) -> InviteVendorsToRFXOutput:
        """Invite vendors to an existing RFX so they can receive and respond to the questionnaire (post_agent_tool_api___invite_vendors_to_rfx)."""
        return cast(
            InviteVendorsToRFXOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/invite-vendors-to-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "rfx_id": rfx_id, "vendors": vendors}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_INVITE_METADATA,
            ),
        )

    def list(
        self,
        *,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListSourcingEventsOutput:
        """List sourcing events visible to the acting user (post_agent_tool_api___list_sourcing_events)."""
        return cast(
            ListSourcingEventsOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-sourcing-events",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_LIST_METADATA,
            ),
        )

    def mark_graded(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> MarkRFXGradedOutput:
        """Mark a PUBLISHED RFX as graded, which unlocks awarding (post_agent_tool_api___mark_rfx_graded)."""
        return cast(
            MarkRFXGradedOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/mark-rfx-graded",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_MARK_GRADED_METADATA,
            ),
        )

    def pricing_sheet(
        self,
        *,
        attachment_ramp_document_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        guidance_markdown: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID,
    ) -> SetRFXPricingSheetOutput:
        """Set or update the pricing sheet on a DRAFT RFX during sourcing intake (post_agent_tool_api___set_rfx_pricing_sheet)."""
        return cast(
            SetRFXPricingSheetOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-pricing-sheet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attachment_ramp_document_ids": attachment_ramp_document_ids,
                        "currency": currency,
                        "guidance_markdown": guidance_markdown,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_PRICING_SHEET_METADATA,
            ),
        )

    def publish(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> PublishRFXOutput:
        """Publish an RFX, sending it externally to every ACTIVE invitation contact (post_agent_tool_api___publish_rfx)."""
        return cast(
            PublishRFXOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/publish-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_PUBLISH_METADATA,
            ),
        )

    def remind(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
        rfx_vendor_invitation_ids: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
    ) -> SendRFXResponseReminderOutput:
        """Send response reminder emails to invited vendors who have not yet (post_agent_tool_api___send_rfx_response_reminder)."""
        return cast(
            SendRFXResponseReminderOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/send-rfx-response-reminder",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                        "rfx_vendor_invitation_ids": rfx_vendor_invitation_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_REMIND_METADATA,
            ),
        )

    def responses(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> RFXVendorResponsesOutput:
        """Return all submitted vendor responses for an RFX (post_agent_tool_api___get_rfx_vendor_responses)."""
        return cast(
            RFXVendorResponsesOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-vendor-responses",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RESPONSES_METADATA,
            ),
        )

    def return_to_draft(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> ReturnRFXToDraftOutput:
        """Return a REJECTED RFX to DRAFT so it can be edited and re-published (post_agent_tool_api___return_rfx_to_draft)."""
        return cast(
            ReturnRFXToDraftOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/return-rfx-to-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RETURN_TO_DRAFT_METADATA,
            ),
        )

    def revoke(
        self,
        *,
        rationale: str,
        rfx_vendor_invitation_id: UUID,
    ) -> RevokeRFXVendorInvitationOutput:
        """Remove a vendor from an RFX (post_agent_tool_api___revoke_rfx_vendor_invitation)."""
        return cast(
            RevokeRFXVendorInvitationOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/revoke-rfx-vendor-invitation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "rfx_vendor_invitation_id": rfx_vendor_invitation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_REVOKE_METADATA,
            ),
        )

    def rfx(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXDetailOutput:
        """Get the full configuration of one RFX: questionnaire sections and fields, (post_agent_tool_api___get_rfx_detail)."""
        return cast(
            GetRFXDetailOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-detail",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RFX_METADATA,
            ),
        )

    def summary(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXResponseSummaryOutput:
        """Summarize vendor response and grading progress for a specific RFX (post_agent_tool_api___get_rfx_response_summary)."""
        return cast(
            GetRFXResponseSummaryOutput,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-response-summary",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_SUMMARY_METADATA,
            ),
        )


class AsyncAgentToolsSourcing:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def award(
        self,
        *,
        payee_uuid: UUID,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> AwardSourcingEventOutput:
        """Award the winning vendor for a sourcing event, deciding the event and (post_agent_tool_api___award_sourcing_event)."""
        return cast(
            AwardSourcingEventOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/award-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "sourcing_event_id": sourcing_event_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_AWARD_METADATA,
            ),
        )

    async def close_event(
        self,
        *,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> CloseSourcingEventOutput:
        """Close (archive) a sourcing event without awarding a vendor (post_agent_tool_api___close_sourcing_event)."""
        return cast(
            CloseSourcingEventOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/close-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sourcing_event_id": sourcing_event_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_CLOSE_EVENT_METADATA,
            ),
        )

    async def collaborators(
        self,
        *,
        add_user_uuids: Sequence[UUID] | NotGiven = NOT_GIVEN,
        rationale: str,
        remove_user_uuids: Sequence[UUID] | NotGiven = NOT_GIVEN,
        rfx_id: UUID,
    ) -> ManageRFXCollaboratorsOutput:
        """Add and/or remove collaborators on an existing RFX (RFI, RFP, or RFQ) (post_agent_tool_api___manage_rfx_collaborators)."""
        return cast(
            ManageRFXCollaboratorsOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/manage-rfx-collaborators",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "add_user_uuids": add_user_uuids,
                        "rationale": rationale,
                        "remove_user_uuids": remove_user_uuids,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_COLLABORATORS_METADATA,
            ),
        )

    async def cover_sheet(
        self,
        *,
        attachment_ramp_document_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        body_markdown: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID,
    ) -> SetRFXCoverSheetOutput:
        """Set or update the vendor-facing cover sheet on a DRAFT RFX (post_agent_tool_api___set_rfx_cover_sheet)."""
        return cast(
            SetRFXCoverSheetOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-cover-sheet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attachment_ramp_document_ids": attachment_ramp_document_ids,
                        "body_markdown": body_markdown,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_COVER_SHEET_METADATA,
            ),
        )

    async def create(
        self,
        *,
        close_date: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        response_submission_deadline: str | None | NotGiven = NOT_GIVEN,
        rfx_type: str | NotGiven = NOT_GIVEN,
        sections: Sequence[dict[str, Any]],
        sourcing_event_id: UUID | None | NotGiven = NOT_GIVEN,
        sourcing_event_name: str | None | NotGiven = NOT_GIVEN,
    ) -> CreateRFXOutput:
        """Create a DRAFT RFX questionnaire, optionally creating its parent sourcing (post_agent_tool_api___create_rfx)."""
        return cast(
            CreateRFXOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_date": close_date,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "response_submission_deadline": response_submission_deadline,
                        "rfx_type": rfx_type,
                        "sections": sections,
                        "sourcing_event_id": sourcing_event_id,
                        "sourcing_event_name": sourcing_event_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_CREATE_METADATA,
            ),
        )

    async def draft_spend_request(
        self,
        *,
        payee_uuid: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID | None | NotGiven = NOT_GIVEN,
        sourcing_event_id: UUID,
        spend_intent_uuid: UUID | None | NotGiven = NOT_GIVEN,
    ) -> CreateDraftSpendRequestFromSourcingEventOutput:
        """Hand off an awarded sourcing event into procurement intake by drafting a (post_agent_tool_api___create_draft_spend_request_from_sourcing_event)."""
        return cast(
            CreateDraftSpendRequestFromSourcingEventOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-draft-spend-request-from-sourcing-event",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                        "sourcing_event_id": sourcing_event_id,
                        "spend_intent_uuid": spend_intent_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_DRAFT_SPEND_REQUEST_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        close_date: str | None | NotGiven = NOT_GIVEN,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        response_submission_deadline: str | None | NotGiven = NOT_GIVEN,
        rfx_id: UUID,
        sections: Sequence[dict[str, Any]],
    ) -> UpdateRFXOutput:
        """Update an RFX's name, description, dates, and questionnaire sections (post_agent_tool_api___update_rfx)."""
        return cast(
            UpdateRFXOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "close_date": close_date,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "response_submission_deadline": response_submission_deadline,
                        "rfx_id": rfx_id,
                        "sections": sections,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_EDIT_METADATA,
            ),
        )

    async def event(
        self,
        *,
        rationale: str,
        sourcing_event_id: UUID,
    ) -> GetSourcingEventContextOutput:
        """Get a compact summary of a sourcing event, its RFXs, and invited vendors (post_agent_tool_api___get_sourcing_event_context)."""
        return cast(
            GetSourcingEventContextOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-sourcing-event-context",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "sourcing_event_id": sourcing_event_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_EVENT_METADATA,
            ),
        )

    async def grading(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXGradingOverviewOutput:
        """Get grading outcomes for an RFX: AI-generated grading insights and (post_agent_tool_api___get_rfx_grading_overview)."""
        return cast(
            GetRFXGradingOverviewOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-grading-overview",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_GRADING_METADATA,
            ),
        )

    async def invitation_contact(
        self,
        *,
        payee_contact_id: UUID,
        rationale: str,
        rfx_vendor_invitation_id: UUID,
    ) -> SetRFXVendorInvitationContactOutput:
        """Set or replace the contact on an RFX vendor invitation (post_agent_tool_api___set_rfx_vendor_invitation_contact)."""
        return cast(
            SetRFXVendorInvitationContactOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-vendor-invitation-contact",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_contact_id": payee_contact_id,
                        "rationale": rationale,
                        "rfx_vendor_invitation_id": rfx_vendor_invitation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_INVITATION_CONTACT_METADATA,
            ),
        )

    async def invite(
        self,
        *,
        rationale: str,
        rfx_id: str,
        vendors: Sequence[dict[str, Any]],
    ) -> InviteVendorsToRFXOutput:
        """Invite vendors to an existing RFX so they can receive and respond to the questionnaire (post_agent_tool_api___invite_vendors_to_rfx)."""
        return cast(
            InviteVendorsToRFXOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/invite-vendors-to-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "rfx_id": rfx_id, "vendors": vendors}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_INVITE_METADATA,
            ),
        )

    async def list(
        self,
        *,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> ListSourcingEventsOutput:
        """List sourcing events visible to the acting user (post_agent_tool_api___list_sourcing_events)."""
        return cast(
            ListSourcingEventsOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-sourcing-events",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_LIST_METADATA,
            ),
        )

    async def mark_graded(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> MarkRFXGradedOutput:
        """Mark a PUBLISHED RFX as graded, which unlocks awarding (post_agent_tool_api___mark_rfx_graded)."""
        return cast(
            MarkRFXGradedOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/mark-rfx-graded",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_MARK_GRADED_METADATA,
            ),
        )

    async def pricing_sheet(
        self,
        *,
        attachment_ramp_document_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        currency: str | None | NotGiven = NOT_GIVEN,
        guidance_markdown: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        rfx_id: UUID,
    ) -> SetRFXPricingSheetOutput:
        """Set or update the pricing sheet on a DRAFT RFX during sourcing intake (post_agent_tool_api___set_rfx_pricing_sheet)."""
        return cast(
            SetRFXPricingSheetOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-rfx-pricing-sheet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attachment_ramp_document_ids": attachment_ramp_document_ids,
                        "currency": currency,
                        "guidance_markdown": guidance_markdown,
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_PRICING_SHEET_METADATA,
            ),
        )

    async def publish(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> PublishRFXOutput:
        """Publish an RFX, sending it externally to every ACTIVE invitation contact (post_agent_tool_api___publish_rfx)."""
        return cast(
            PublishRFXOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/publish-rfx",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_PUBLISH_METADATA,
            ),
        )

    async def remind(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
        rfx_vendor_invitation_ids: Sequence[UUID] | None | NotGiven = NOT_GIVEN,
    ) -> SendRFXResponseReminderOutput:
        """Send response reminder emails to invited vendors who have not yet (post_agent_tool_api___send_rfx_response_reminder)."""
        return cast(
            SendRFXResponseReminderOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/send-rfx-response-reminder",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "rfx_id": rfx_id,
                        "rfx_vendor_invitation_ids": rfx_vendor_invitation_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_REMIND_METADATA,
            ),
        )

    async def responses(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> RFXVendorResponsesOutput:
        """Return all submitted vendor responses for an RFX (post_agent_tool_api___get_rfx_vendor_responses)."""
        return cast(
            RFXVendorResponsesOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-vendor-responses",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RESPONSES_METADATA,
            ),
        )

    async def return_to_draft(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> ReturnRFXToDraftOutput:
        """Return a REJECTED RFX to DRAFT so it can be edited and re-published (post_agent_tool_api___return_rfx_to_draft)."""
        return cast(
            ReturnRFXToDraftOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/return-rfx-to-draft",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RETURN_TO_DRAFT_METADATA,
            ),
        )

    async def revoke(
        self,
        *,
        rationale: str,
        rfx_vendor_invitation_id: UUID,
    ) -> RevokeRFXVendorInvitationOutput:
        """Remove a vendor from an RFX (post_agent_tool_api___revoke_rfx_vendor_invitation)."""
        return cast(
            RevokeRFXVendorInvitationOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/revoke-rfx-vendor-invitation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "rfx_vendor_invitation_id": rfx_vendor_invitation_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_REVOKE_METADATA,
            ),
        )

    async def rfx(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXDetailOutput:
        """Get the full configuration of one RFX: questionnaire sections and fields, (post_agent_tool_api___get_rfx_detail)."""
        return cast(
            GetRFXDetailOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-detail",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_RFX_METADATA,
            ),
        )

    async def summary(
        self,
        *,
        rationale: str,
        rfx_id: UUID,
    ) -> GetRFXResponseSummaryOutput:
        """Summarize vendor response and grading progress for a specific RFX (post_agent_tool_api___get_rfx_response_summary)."""
        return cast(
            GetRFXResponseSummaryOutput,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-rfx-response-summary",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "rfx_id": rfx_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_SOURCING_SUMMARY_METADATA,
            ),
        )


class AgentToolsStatements:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def outstanding(
        self,
        *,
        rationale: str,
    ) -> CardStatementBalanceJsonMode:
        """Get a snapshot of the business's most recent card statement balance — (post_agent_tool_api___get_card_statement_balance)."""
        return cast(
            CardStatementBalanceJsonMode,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-card-statement-balance",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_STATEMENTS_OUTSTANDING_METADATA,
            ),
        )


class AsyncAgentToolsStatements:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def outstanding(
        self,
        *,
        rationale: str,
    ) -> CardStatementBalanceJsonMode:
        """Get a snapshot of the business's most recent card statement balance — (post_agent_tool_api___get_card_statement_balance)."""
        return cast(
            CardStatementBalanceJsonMode,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-card-statement-balance",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_STATEMENTS_OUTSTANDING_METADATA,
            ),
        )


class AgentToolsTasks:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(
        self,
        *,
        fanout_timeout_seconds: float | NotGiven = NOT_GIVEN,
        rationale: str,
        sections: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
    ) -> GetAttentionFeedResult:
        """Return the authenticated user's homepage attention feed (post_agent_tool_api___get_attention_feed)."""
        return cast(
            GetAttentionFeedResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-attention-feed",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "fanout_timeout_seconds": fanout_timeout_seconds,
                        "rationale": rationale,
                        "sections": sections,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TASKS_LIST_METADATA,
            ),
        )


class AsyncAgentToolsTasks:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self,
        *,
        fanout_timeout_seconds: float | NotGiven = NOT_GIVEN,
        rationale: str,
        sections: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
    ) -> GetAttentionFeedResult:
        """Return the authenticated user's homepage attention feed (post_agent_tool_api___get_attention_feed)."""
        return cast(
            GetAttentionFeedResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-attention-feed",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "fanout_timeout_seconds": fanout_timeout_seconds,
                        "rationale": rationale,
                        "sections": sections,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TASKS_LIST_METADATA,
            ),
        )


class AgentToolsTransactions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def approve(
        self,
        *,
        action: str,
        rationale: str,
        thoughts: str,
        transaction_id: str,
        user_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> TransactionActionResult:
        """Approve or reject a transaction awaiting your review (post_agent_tool_api___approve_or_reject_transaction)."""
        return cast(
            TransactionActionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "thoughts": thoughts,
                        "transaction_id": transaction_id,
                        "user_reason": user_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_APPROVE_METADATA,
            ),
        )

    def complete_revision(
        self,
        *,
        rationale: str,
        reason: str,
        transaction_uuid: UUID,
    ) -> CompleteTransactionRevisionResult:
        """Complete a revision-requested transaction as its cardholder (post_agent_tool_api___complete_transaction_revision)."""
        return cast(
            CompleteTransactionRevisionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/complete-transaction-revision",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_COMPLETE_REVISION_METADATA,
            ),
        )

    def edit(
        self,
        *,
        attendee_selections: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        memo: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        tracking_category_selections: Sequence[dict[str, Any]]
        | None
        | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None,
        trip_selection: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        user_submitted_fields: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> EditTransactionSuccess:
        """Edit a transaction field (memo, funds, accounting categories, trip, attendees) (post_agent_tool_api___edit_transaction)."""
        return cast(
            EditTransactionSuccess,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attendee_selections": attendee_selections,
                        "fund_uuid": fund_uuid,
                        "memo": memo,
                        "rationale": rationale,
                        "tracking_category_selections": tracking_category_selections,
                        "transaction_uuid": transaction_uuid,
                        "trip_selection": trip_selection,
                        "user_submitted_fields": user_submitted_fields,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_EDIT_METADATA,
            ),
        )

    def explain_missing(
        self,
        *,
        rationale: str,
        reason: str,
        transaction_uuid: str | None,
    ) -> ProvideNoReceiptReasonResponse:
        """Submit a reason explaining why a transaction has no receipt (post_agent_tool_api___provide_no_receipt_reason)."""
        return cast(
            ProvideNoReceiptReasonResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/provide-no-receipt-reason",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_EXPLAIN_MISSING_METADATA,
            ),
        )

    def flag_missing(
        self,
        *,
        rationale: str,
        transaction_uuid: str | None,
    ) -> MarkTransactionMissingReceiptResponse:
        """Flag a transaction as having no receipt (post_agent_tool_api___mark_transaction_missing_receipt)."""
        return cast(
            MarkTransactionMissingReceiptResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/mark-transaction-missing-receipt",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "transaction_uuid": transaction_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_FLAG_MISSING_METADATA,
            ),
        )

    def get(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> FullTransactionMetadata:
        """View all details, memos, funds, and receipts for a specific transaction (post_agent_tool_api___get_full_transaction_metadata)."""
        return cast(
            FullTransactionMetadata,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-full-transaction-metadata",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_GET_METADATA,
            ),
        )

    def list(
        self,
        *,
        details_to_include_in_response: Sequence[str] | None | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        include_count: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reason_memo_merchant_or_user_name_text_search: str
        | None
        | NotGiven = NOT_GIVEN,
        sort: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        state: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
        transactions_to_retrieve: str,
    ) -> GetTransactionsResult:
        """Search and retrieve individual card transactions and workflow details for the user's business, including reconciliation dates (cleared_at, settlement_date, accounting_date, synced_at) and, via details_to_include_in_response=['submitted_items'], the selected accounting categories (post_agent_tool_api___get_user_transactions)."""
        return cast(
            GetTransactionsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transactions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "details_to_include_in_response": details_to_include_in_response,
                        "filters": filters,
                        "from_date": from_date,
                        "include_count": include_count,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reason_memo_merchant_or_user_name_text_search": reason_memo_merchant_or_user_name_text_search,
                        "sort": sort,
                        "state": state,
                        "to_date": to_date,
                        "transactions_to_retrieve": transactions_to_retrieve,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_LIST_METADATA,
            ),
        )

    def memo_suggestions(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> SuggestedMemos:
        """Get AI-suggested memo/note options for a specific transaction (post_agent_tool_api___get_transaction_suggested_memos)."""
        return cast(
            SuggestedMemos,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transaction-suggested-memos",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MEMO_SUGGESTIONS_METADATA,
            ),
        )

    def missing(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> TransactionMissingItems:
        """Check what receipts, memos, or accounting items are missing from a specific transaction (post_agent_tool_api___get_transaction_missing_items)."""
        return cast(
            TransactionMissingItems,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transaction-missing-items",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MISSING_METADATA,
            ),
        )

    def missing_by_user(
        self,
        *,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        user_limit: int | NotGiven = NOT_GIVEN,
    ) -> GetMissingItemsByUserResult:
        """Get transactions with missing items (receipts or memos) grouped by user (get_agent_tool_api___get_missing_items_by_user)."""
        return cast(
            GetMissingItemsByUserResult,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-missing-items-by-user",
                path_params=None,
                params=_without_not_given(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "user_limit": user_limit,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MISSING_BY_USER_METADATA,
            ),
        )

    def request_repayment(
        self,
        *,
        rationale: str,
        reason: str,
        thoughts: str,
        transaction_id: str,
    ) -> RepaymentRequestResult:
        """Request that a cardholder repay a transaction (post_agent_tool_api___request_transaction_repayment)."""
        return cast(
            RepaymentRequestResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/request-transaction-repayment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "thoughts": thoughts,
                        "transaction_id": transaction_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_REQUEST_REPAYMENT_METADATA,
            ),
        )

    def search_suggested_users(
        self,
        *,
        rationale: str,
        search: str,
        transaction_id: str | None | NotGiven = NOT_GIVEN,
    ) -> SearchUserResponse:
        """Match a user name to a Ramp user in the context of a transaction, for adding as an attendee (post_agent_tool_api___match_user_to_transaction)."""
        return cast(
            SearchUserResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-user",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "search": search,
                        "transaction_id": transaction_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_SEARCH_SUGGESTED_USERS_METADATA,
            ),
        )

    def trips(
        self,
        *,
        rationale: str,
    ) -> CandidateTripsResult:
        """Fetch trips that could be relevant to the current transaction (post_agent_tool_api___get_candidate_trips_for_transaction)."""
        return cast(
            CandidateTripsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-candidate-trips-for-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_TRIPS_METADATA,
            ),
        )


class AsyncAgentToolsTransactions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def approve(
        self,
        *,
        action: str,
        rationale: str,
        thoughts: str,
        transaction_id: str,
        user_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> TransactionActionResult:
        """Approve or reject a transaction awaiting your review (post_agent_tool_api___approve_or_reject_transaction)."""
        return cast(
            TransactionActionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/approve-or-reject-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "rationale": rationale,
                        "thoughts": thoughts,
                        "transaction_id": transaction_id,
                        "user_reason": user_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_APPROVE_METADATA,
            ),
        )

    async def complete_revision(
        self,
        *,
        rationale: str,
        reason: str,
        transaction_uuid: UUID,
    ) -> CompleteTransactionRevisionResult:
        """Complete a revision-requested transaction as its cardholder (post_agent_tool_api___complete_transaction_revision)."""
        return cast(
            CompleteTransactionRevisionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/complete-transaction-revision",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_COMPLETE_REVISION_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        attendee_selections: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        fund_uuid: str | None | NotGiven = NOT_GIVEN,
        memo: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        tracking_category_selections: Sequence[dict[str, Any]]
        | None
        | NotGiven = NOT_GIVEN,
        transaction_uuid: str | None,
        trip_selection: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        user_submitted_fields: Sequence[str] | NotGiven = NOT_GIVEN,
    ) -> EditTransactionSuccess:
        """Edit a transaction field (memo, funds, accounting categories, trip, attendees) (post_agent_tool_api___edit_transaction)."""
        return cast(
            EditTransactionSuccess,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/edit-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "attendee_selections": attendee_selections,
                        "fund_uuid": fund_uuid,
                        "memo": memo,
                        "rationale": rationale,
                        "tracking_category_selections": tracking_category_selections,
                        "transaction_uuid": transaction_uuid,
                        "trip_selection": trip_selection,
                        "user_submitted_fields": user_submitted_fields,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_EDIT_METADATA,
            ),
        )

    async def explain_missing(
        self,
        *,
        rationale: str,
        reason: str,
        transaction_uuid: str | None,
    ) -> ProvideNoReceiptReasonResponse:
        """Submit a reason explaining why a transaction has no receipt (post_agent_tool_api___provide_no_receipt_reason)."""
        return cast(
            ProvideNoReceiptReasonResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/provide-no-receipt-reason",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "transaction_uuid": transaction_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_EXPLAIN_MISSING_METADATA,
            ),
        )

    async def flag_missing(
        self,
        *,
        rationale: str,
        transaction_uuid: str | None,
    ) -> MarkTransactionMissingReceiptResponse:
        """Flag a transaction as having no receipt (post_agent_tool_api___mark_transaction_missing_receipt)."""
        return cast(
            MarkTransactionMissingReceiptResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/mark-transaction-missing-receipt",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "transaction_uuid": transaction_uuid}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_FLAG_MISSING_METADATA,
            ),
        )

    async def get(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> FullTransactionMetadata:
        """View all details, memos, funds, and receipts for a specific transaction (post_agent_tool_api___get_full_transaction_metadata)."""
        return cast(
            FullTransactionMetadata,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-full-transaction-metadata",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_GET_METADATA,
            ),
        )

    async def list(
        self,
        *,
        details_to_include_in_response: Sequence[str] | None | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        include_count: bool | NotGiven = NOT_GIVEN,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        reason_memo_merchant_or_user_name_text_search: str
        | None
        | NotGiven = NOT_GIVEN,
        sort: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        state: str | None | NotGiven = NOT_GIVEN,
        to_date: str | None | NotGiven = NOT_GIVEN,
        transactions_to_retrieve: str,
    ) -> GetTransactionsResult:
        """Search and retrieve individual card transactions and workflow details for the user's business, including reconciliation dates (cleared_at, settlement_date, accounting_date, synced_at) and, via details_to_include_in_response=['submitted_items'], the selected accounting categories (post_agent_tool_api___get_user_transactions)."""
        return cast(
            GetTransactionsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transactions",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "details_to_include_in_response": details_to_include_in_response,
                        "filters": filters,
                        "from_date": from_date,
                        "include_count": include_count,
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "reason_memo_merchant_or_user_name_text_search": reason_memo_merchant_or_user_name_text_search,
                        "sort": sort,
                        "state": state,
                        "to_date": to_date,
                        "transactions_to_retrieve": transactions_to_retrieve,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_LIST_METADATA,
            ),
        )

    async def memo_suggestions(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> SuggestedMemos:
        """Get AI-suggested memo/note options for a specific transaction (post_agent_tool_api___get_transaction_suggested_memos)."""
        return cast(
            SuggestedMemos,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transaction-suggested-memos",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MEMO_SUGGESTIONS_METADATA,
            ),
        )

    async def missing(
        self,
        *,
        id: UUID | None,
        rationale: str,
    ) -> TransactionMissingItems:
        """Check what receipts, memos, or accounting items are missing from a specific transaction (post_agent_tool_api___get_transaction_missing_items)."""
        return cast(
            TransactionMissingItems,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-transaction-missing-items",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"id": id, "rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MISSING_METADATA,
            ),
        )

    async def missing_by_user(
        self,
        *,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        user_limit: int | NotGiven = NOT_GIVEN,
    ) -> GetMissingItemsByUserResult:
        """Get transactions with missing items (receipts or memos) grouped by user (get_agent_tool_api___get_missing_items_by_user)."""
        return cast(
            GetMissingItemsByUserResult,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-missing-items-by-user",
                path_params=None,
                params=_without_not_given(
                    {
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "user_limit": user_limit,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_MISSING_BY_USER_METADATA,
            ),
        )

    async def request_repayment(
        self,
        *,
        rationale: str,
        reason: str,
        thoughts: str,
        transaction_id: str,
    ) -> RepaymentRequestResult:
        """Request that a cardholder repay a transaction (post_agent_tool_api___request_transaction_repayment)."""
        return cast(
            RepaymentRequestResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/request-transaction-repayment",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "reason": reason,
                        "thoughts": thoughts,
                        "transaction_id": transaction_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_REQUEST_REPAYMENT_METADATA,
            ),
        )

    async def search_suggested_users(
        self,
        *,
        rationale: str,
        search: str,
        transaction_id: str | None | NotGiven = NOT_GIVEN,
    ) -> SearchUserResponse:
        """Match a user name to a Ramp user in the context of a transaction, for adding as an attendee (post_agent_tool_api___match_user_to_transaction)."""
        return cast(
            SearchUserResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-user",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "search": search,
                        "transaction_id": transaction_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_SEARCH_SUGGESTED_USERS_METADATA,
            ),
        )

    async def trips(
        self,
        *,
        rationale: str,
    ) -> CandidateTripsResult:
        """Fetch trips that could be relevant to the current transaction (post_agent_tool_api___get_candidate_trips_for_transaction)."""
        return cast(
            CandidateTripsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-candidate-trips-for-transaction",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRANSACTIONS_TRIPS_METADATA,
            ),
        )


class AgentToolsTravel:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def add_traveler_loyalty_program(
        self,
        *,
        loyalty_number: str,
        program_name: str,
        rationale: str,
    ) -> SetTravelerLoyaltyProgramResult:
        """Compatibility route for callers that have not migrated to SetTravelerLoyaltyProgram (post_agent_tool_api___traveler_loyalty_program_legacy_setter)."""
        return cast(
            SetTravelerLoyaltyProgramResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/add-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "program_name": program_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_ADD_TRAVELER_LOYALTY_PROGRAM_METADATA,
            ),
        )

    def approve(
        self,
        *,
        action: str,
        booking_request_id: str,
        rationale: str,
        rejection_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> TravelRequestActionResult:
        """Approve or reject a travel/booking request (post_agent_tool_api___travel_request_action)."""
        return cast(
            TravelRequestActionResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/travel-request-action",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "booking_request_id": booking_request_id,
                        "rationale": rationale,
                        "rejection_reason": rejection_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_APPROVE_METADATA,
            ),
        )

    def book_flight(
        self,
        *,
        confirm: bool | NotGiven = NOT_GIVEN,
        expected_total_amount: Any | None | NotGiven = NOT_GIVEN,
        flight_offer_uuid: UUID,
        oop_reason: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_new_fund: bool | NotGiven = NOT_GIVEN,
        selection_surface_call_id: str | None | NotGiven = NOT_GIVEN,
        simulate: bool | NotGiven = NOT_GIVEN,
        spend_allocation_id: UUID | None | NotGiven = NOT_GIVEN,
        traveler_user_id: UUID | None | NotGiven = NOT_GIVEN,
        trip_id: UUID | None | NotGiven = NOT_GIVEN,
    ) -> FlightBookingResult:
        """Book a selected flight offer (post_agent_tool_api___submit_flight_booking)."""
        return cast(
            FlightBookingResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-flight-booking",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirm": confirm,
                        "expected_total_amount": expected_total_amount,
                        "flight_offer_uuid": flight_offer_uuid,
                        "oop_reason": oop_reason,
                        "rationale": rationale,
                        "reason": reason,
                        "request_new_fund": request_new_fund,
                        "selection_surface_call_id": selection_surface_call_id,
                        "simulate": simulate,
                        "spend_allocation_id": spend_allocation_id,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOK_FLIGHT_METADATA,
            ),
        )

    def book_hotel(
        self,
        *,
        check_in_date: str,
        check_out_date: str,
        confirm: bool | NotGiven = NOT_GIVEN,
        expected_total_amount: Any | None | NotGiven = NOT_GIVEN,
        hotel_id: UUID,
        oop_reason: str | None | NotGiven = NOT_GIVEN,
        rate_id: UUID,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_new_fund: bool | NotGiven = NOT_GIVEN,
        selection_surface_call_id: str | None | NotGiven = NOT_GIVEN,
        spend_allocation_id: UUID | None | NotGiven = NOT_GIVEN,
        traveler_user_id: UUID | None | NotGiven = NOT_GIVEN,
        trip_id: UUID | None | NotGiven = NOT_GIVEN,
    ) -> HotelBookingResult:
        """Book a selected hotel rate (post_agent_tool_api___submit_hotel_booking)."""
        return cast(
            HotelBookingResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-hotel-booking",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "confirm": confirm,
                        "expected_total_amount": expected_total_amount,
                        "hotel_id": hotel_id,
                        "oop_reason": oop_reason,
                        "rate_id": rate_id,
                        "rationale": rationale,
                        "reason": reason,
                        "request_new_fund": request_new_fund,
                        "selection_surface_call_id": selection_surface_call_id,
                        "spend_allocation_id": spend_allocation_id,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOK_HOTEL_METADATA,
            ),
        )

    def booking_details(
        self,
        *,
        booking_id: UUID,
        rationale: str,
    ) -> BookingDetails:
        """Get itinerary, stay, or rental details plus request status, amount, payment timing, cancellation state, associated spend, error, and approval information for one exact UUID from GetBookings (post_agent_tool_api___get_booking_details)."""
        return cast(
            BookingDetails,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-booking-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"booking_id": booking_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOKING_DETAILS_METADATA,
            ),
        )

    def bookings(
        self,
        *,
        booking_reference: str | None | NotGiven = NOT_GIVEN,
        city: str | None | NotGiven = NOT_GIVEN,
        flight_airline: str | None | NotGiven = NOT_GIVEN,
        flight_number: str | None | NotGiven = NOT_GIVEN,
        hotel_name: str | None | NotGiven = NOT_GIVEN,
        include_cars: bool | NotGiven = NOT_GIVEN,
        include_failed: bool | NotGiven = NOT_GIVEN,
        include_flights: bool | NotGiven = NOT_GIVEN,
        include_hotels: bool | NotGiven = NOT_GIVEN,
        include_past: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
        travel_date: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        verification_mode: bool | NotGiven = NOT_GIVEN,
    ) -> BookingsResult:
        """Retrieve flight, hotel, and car rental booking summaries for the user (post_agent_tool_api___get_bookings)."""
        return cast(
            BookingsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bookings",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_reference": booking_reference,
                        "city": city,
                        "flight_airline": flight_airline,
                        "flight_number": flight_number,
                        "hotel_name": hotel_name,
                        "include_cars": include_cars,
                        "include_failed": include_failed,
                        "include_flights": include_flights,
                        "include_hotels": include_hotels,
                        "include_past": include_past,
                        "limit": limit,
                        "rationale": rationale,
                        "travel_date": travel_date,
                        "traveler_user_id": traveler_user_id,
                        "verification_mode": verification_mode,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOKINGS_METADATA,
            ),
        )

    def cancel_flight(
        self,
        *,
        booking_id: UUID,
        confirm: bool | NotGiven = NOT_GIVEN,
        preview_id: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> FlightCancellationResponse:
        """Preview or confirm cancellation of an existing flight booking (post_agent_tool_api___submit_flight_cancellation)."""
        return cast(
            FlightCancellationResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-flight-cancellation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_id": booking_id,
                        "confirm": confirm,
                        "preview_id": preview_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CANCEL_FLIGHT_METADATA,
            ),
        )

    def cancel_hotel(
        self,
        *,
        booking_id: UUID,
        confirm: bool | NotGiven = NOT_GIVEN,
        preview_id: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> HotelCancellationResponse:
        """Preview or confirm cancellation of an existing hotel booking (post_agent_tool_api___submit_hotel_cancellation)."""
        return cast(
            HotelCancellationResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-hotel-cancellation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_id": booking_id,
                        "confirm": confirm,
                        "preview_id": preview_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CANCEL_HOTEL_METADATA,
            ),
        )

    def create(
        self,
        *,
        are_trip_dates_from_booking_receipt_or_user_input: bool,
        calendar_timezone: str | None | NotGiven = NOT_GIVEN,
        destinations: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        end_date: Any | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        start_date: Any | None | NotGiven = NOT_GIVEN,
        trip_purpose: str | None | NotGiven = NOT_GIVEN,
    ) -> TripCreationResult:
        """Create a new trip for the acting user (post_agent_tool_api___create_trip)."""
        return cast(
            TripCreationResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-trip",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "are_trip_dates_from_booking_receipt_or_user_input": are_trip_dates_from_booking_receipt_or_user_input,
                        "calendar_timezone": calendar_timezone,
                        "destinations": destinations,
                        "end_date": end_date,
                        "name": name,
                        "rationale": rationale,
                        "start_date": start_date,
                        "trip_purpose": trip_purpose,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CREATE_METADATA,
            ),
        )

    def hotel_rates(
        self,
        *,
        check_in_date: str,
        check_out_date: str,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        hotel_id: str,
        max_recommended_rates: int | NotGiven = NOT_GIVEN,
        num_adults: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_id: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> GetHotelRatesResult:
        """Fetch available room-rate options for one selected hotel from SearchHotels (post_agent_tool_api___get_hotel_rates)."""
        return cast(
            GetHotelRatesResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-hotel-rates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "filters": filters,
                        "hotel_id": hotel_id,
                        "max_recommended_rates": max_recommended_rates,
                        "num_adults": num_adults,
                        "rationale": rationale,
                        "search_id": search_id,
                        "traveler_user_id": traveler_user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_HOTEL_RATES_METADATA,
            ),
        )

    def list(
        self,
        *,
        cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | None | NotGiven = NOT_GIVEN,
        rationale: str,
        status: str | None | NotGiven = NOT_GIVEN,
    ) -> TripListResult:
        """Fetch trips for the acting user with optional filters (post_agent_tool_api___get_user_trips)."""
        return cast(
            TripListResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-user-trips",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "status": status,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LIST_METADATA,
            ),
        )

    def locations(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        location_type: str | NotGiven = NOT_GIVEN,
        query: str,
        rationale: str,
    ) -> FlightLocationSearchResult:
        """Resolves locations (airports/cities) available for booking a flight from user intent (post_agent_tool_api___get_flight_booking_locations)."""
        return cast(
            FlightLocationSearchResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-flight-booking-locations",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "limit": limit,
                        "location_type": location_type,
                        "query": query,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOCATIONS_METADATA,
            ),
        )

    def loyalty_program_remove(
        self,
        *,
        rationale: str,
        traveler_loyalty_program_id: str,
    ) -> RemoveTravelerLoyaltyProgramResult:
        """Remove a saved loyalty program from the user's traveler profile (post_agent_tool_api___remove_traveler_loyalty_program)."""
        return cast(
            RemoveTravelerLoyaltyProgramResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remove-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "traveler_loyalty_program_id": traveler_loyalty_program_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_REMOVE_METADATA,
            ),
        )

    def loyalty_program_set(
        self,
        *,
        loyalty_number: str,
        program_name: str,
        rationale: str,
    ) -> SetTravelerLoyaltyProgramResult:
        """Set one loyalty program on the user's traveler profile by program name and loyalty number (post_agent_tool_api___set_traveler_loyalty_program)."""
        return cast(
            SetTravelerLoyaltyProgramResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "program_name": program_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_SET_METADATA,
            ),
        )

    def loyalty_programs(
        self,
        *,
        rationale: str,
    ) -> ListTravelerLoyaltyProgramsResult:
        """List saved loyalty programs from the user's traveler profile (post_agent_tool_api___list_traveler_loyalty_programs)."""
        return cast(
            ListTravelerLoyaltyProgramsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-traveler-loyalty-programs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAMS_METADATA,
            ),
        )

    def offices(
        self,
        *,
        rationale: str,
    ) -> GetOfficeLocationsResult:
        """Retrieve the company's office locations and addresses (post_agent_tool_api___get_office_locations)."""
        return cast(
            GetOfficeLocationsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-office-locations",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_OFFICES_METADATA,
            ),
        )

    def pending(
        self,
        *,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> TravelRequestListResult:
        """Retrieves travel/booking requests that are pending approval from the current user (post_agent_tool_api___get_pending_travel_requests)."""
        return cast(
            TravelRequestListResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-pending-travel-requests",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PENDING_METADATA,
            ),
        )

    def profile(
        self,
        *,
        rationale: str,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTravelerProfileResult:
        """Retrieve traveler profile information including name, email, phone, date of birth, gender, known traveler number (KTN/TSA), redress number, and loyalty programs (post_agent_tool_api___get_traveler_profile)."""
        return cast(
            GetTravelerProfileResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-traveler-profile",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "traveler_user_id": traveler_user_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PROFILE_METADATA,
            ),
        )

    def profile_update(
        self,
        *,
        avoid_red_eye_flights: bool | NotGiven = NOT_GIVEN,
        date_of_birth: str | None | NotGiven = NOT_GIVEN,
        email: str | None | NotGiven = NOT_GIVEN,
        first_name: str | None | NotGiven = NOT_GIVEN,
        home_airport_code: str | None | NotGiven = NOT_GIVEN,
        id_gender: str | None | NotGiven = NOT_GIVEN,
        known_traveler_number: str | None | NotGiven = NOT_GIVEN,
        last_name: str | None | NotGiven = NOT_GIVEN,
        loyalty_programs: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        max_stops: int | None | NotGiven = NOT_GIVEN,
        middle_name: str | None | NotGiven = NOT_GIVEN,
        name_prefix: str | None | NotGiven = NOT_GIVEN,
        name_suffix: str | None | NotGiven = NOT_GIVEN,
        phone_country_code: str | None | NotGiven = NOT_GIVEN,
        phone_number: str | None | NotGiven = NOT_GIVEN,
        preferred_airlines: Sequence[str] | NotGiven = NOT_GIVEN,
        preferred_arrival_time_window: str | None | NotGiven = NOT_GIVEN,
        preferred_cabin_class: str | None | NotGiven = NOT_GIVEN,
        preferred_departure_time_window: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        redress_number: str | None | NotGiven = NOT_GIVEN,
        seat_preference: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> UpdateTravelerProfileResult:
        """Update traveler identity and contact profile details (post_agent_tool_api___update_traveler_profile)."""
        return cast(
            UpdateTravelerProfileResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-traveler-profile",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "avoid_red_eye_flights": avoid_red_eye_flights,
                        "date_of_birth": date_of_birth,
                        "email": email,
                        "first_name": first_name,
                        "home_airport_code": home_airport_code,
                        "id_gender": id_gender,
                        "known_traveler_number": known_traveler_number,
                        "last_name": last_name,
                        "loyalty_programs": loyalty_programs,
                        "max_stops": max_stops,
                        "middle_name": middle_name,
                        "name_prefix": name_prefix,
                        "name_suffix": name_suffix,
                        "phone_country_code": phone_country_code,
                        "phone_number": phone_number,
                        "preferred_airlines": preferred_airlines,
                        "preferred_arrival_time_window": preferred_arrival_time_window,
                        "preferred_cabin_class": preferred_cabin_class,
                        "preferred_departure_time_window": preferred_departure_time_window,
                        "rationale": rationale,
                        "redress_number": redress_number,
                        "seat_preference": seat_preference,
                        "traveler_user_id": traveler_user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PROFILE_UPDATE_METADATA,
            ),
        )

    def search_flight(
        self,
        *,
        airlines: Sequence[str] | None | NotGiven = NOT_GIVEN,
        arrival: str | None | NotGiven = NOT_GIVEN,
        avoid_red_eye_flights: bool | None | NotGiven = NOT_GIVEN,
        cabin_class: Any | None | NotGiven = NOT_GIVEN,
        clear_preferences: Sequence[str] | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        departure: str | None | NotGiven = NOT_GIVEN,
        departure_date: str | None | NotGiven = NOT_GIVEN,
        include_fare_options: bool | NotGiven = NOT_GIVEN,
        job_id: str | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_stops: int | None | NotGiven = NOT_GIVEN,
        only_split_tickets: bool | None | NotGiven = NOT_GIVEN,
        outbound_offer_id: str | None | NotGiven = NOT_GIVEN,
        preferred_arrival_time_window: str | None | NotGiven = NOT_GIVEN,
        preferred_departure_time_window: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        requested_weekday: str | None | NotGiven = NOT_GIVEN,
        return_date: str | None | NotGiven = NOT_GIVEN,
        sort_key: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        trip_id: str | None | NotGiven = NOT_GIVEN,
        wait_for_results: bool | NotGiven = NOT_GIVEN,
    ) -> SearchFlightsResult:
        """Search for flights and return policy-tagged offers ready to quote (post_agent_tool_api___search_flights)."""
        return cast(
            SearchFlightsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-flights",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "airlines": airlines,
                        "arrival": arrival,
                        "avoid_red_eye_flights": avoid_red_eye_flights,
                        "cabin_class": cabin_class,
                        "clear_preferences": clear_preferences,
                        "cursor": cursor,
                        "departure": departure,
                        "departure_date": departure_date,
                        "include_fare_options": include_fare_options,
                        "job_id": job_id,
                        "limit": limit,
                        "max_stops": max_stops,
                        "only_split_tickets": only_split_tickets,
                        "outbound_offer_id": outbound_offer_id,
                        "preferred_arrival_time_window": preferred_arrival_time_window,
                        "preferred_departure_time_window": preferred_departure_time_window,
                        "rationale": rationale,
                        "requested_weekday": requested_weekday,
                        "return_date": return_date,
                        "sort_key": sort_key,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                        "wait_for_results": wait_for_results,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_SEARCH_FLIGHT_METADATA,
            ),
        )

    def search_hotel(
        self,
        *,
        check_in_date: str | None | NotGiven = NOT_GIVEN,
        check_out_date: str | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        hotel_name: str | None | NotGiven = NOT_GIVEN,
        latitude: Any | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location_query: str | None | NotGiven = NOT_GIVEN,
        longitude: Any | None | NotGiven = NOT_GIVEN,
        num_adults: int | NotGiven = NOT_GIVEN,
        preferences: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        search_id: str | None | NotGiven = NOT_GIVEN,
        sort: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        wait_for_results: bool | None | NotGiven = NOT_GIVEN,
    ) -> SearchHotelsResult:
        """Search hotels using the canonical Ramp web inventory and policy flow (post_agent_tool_api___search_hotels)."""
        return cast(
            SearchHotelsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-hotel",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "cursor": cursor,
                        "filters": filters,
                        "hotel_name": hotel_name,
                        "latitude": latitude,
                        "limit": limit,
                        "location_query": location_query,
                        "longitude": longitude,
                        "num_adults": num_adults,
                        "preferences": preferences,
                        "rationale": rationale,
                        "search_id": search_id,
                        "sort": sort,
                        "traveler_user_id": traveler_user_id,
                        "wait_for_results": wait_for_results,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_SEARCH_HOTEL_METADATA,
            ),
        )

    def update_traveler_loyalty_program(
        self,
        *,
        loyalty_number: str,
        rationale: str,
        traveler_loyalty_program_id: str,
    ) -> TravelerLoyaltyProgramCompatibilityResult:
        """Compatibility route for callers that still update a saved loyalty program by ID (post_agent_tool_api___traveler_loyalty_program_number_setter)."""
        return cast(
            TravelerLoyaltyProgramCompatibilityResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "rationale": rationale,
                        "traveler_loyalty_program_id": traveler_loyalty_program_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_UPDATE_TRAVELER_LOYALTY_PROGRAM_METADATA,
            ),
        )


class AsyncAgentToolsTravel:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def add_traveler_loyalty_program(
        self,
        *,
        loyalty_number: str,
        program_name: str,
        rationale: str,
    ) -> SetTravelerLoyaltyProgramResult:
        """Compatibility route for callers that have not migrated to SetTravelerLoyaltyProgram (post_agent_tool_api___traveler_loyalty_program_legacy_setter)."""
        return cast(
            SetTravelerLoyaltyProgramResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/add-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "program_name": program_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_ADD_TRAVELER_LOYALTY_PROGRAM_METADATA,
            ),
        )

    async def approve(
        self,
        *,
        action: str,
        booking_request_id: str,
        rationale: str,
        rejection_reason: str | None | NotGiven = NOT_GIVEN,
    ) -> TravelRequestActionResult:
        """Approve or reject a travel/booking request (post_agent_tool_api___travel_request_action)."""
        return cast(
            TravelRequestActionResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/travel-request-action",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "action": action,
                        "booking_request_id": booking_request_id,
                        "rationale": rationale,
                        "rejection_reason": rejection_reason,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_APPROVE_METADATA,
            ),
        )

    async def book_flight(
        self,
        *,
        confirm: bool | NotGiven = NOT_GIVEN,
        expected_total_amount: Any | None | NotGiven = NOT_GIVEN,
        flight_offer_uuid: UUID,
        oop_reason: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_new_fund: bool | NotGiven = NOT_GIVEN,
        selection_surface_call_id: str | None | NotGiven = NOT_GIVEN,
        simulate: bool | NotGiven = NOT_GIVEN,
        spend_allocation_id: UUID | None | NotGiven = NOT_GIVEN,
        traveler_user_id: UUID | None | NotGiven = NOT_GIVEN,
        trip_id: UUID | None | NotGiven = NOT_GIVEN,
    ) -> FlightBookingResult:
        """Book a selected flight offer (post_agent_tool_api___submit_flight_booking)."""
        return cast(
            FlightBookingResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-flight-booking",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "confirm": confirm,
                        "expected_total_amount": expected_total_amount,
                        "flight_offer_uuid": flight_offer_uuid,
                        "oop_reason": oop_reason,
                        "rationale": rationale,
                        "reason": reason,
                        "request_new_fund": request_new_fund,
                        "selection_surface_call_id": selection_surface_call_id,
                        "simulate": simulate,
                        "spend_allocation_id": spend_allocation_id,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOK_FLIGHT_METADATA,
            ),
        )

    async def book_hotel(
        self,
        *,
        check_in_date: str,
        check_out_date: str,
        confirm: bool | NotGiven = NOT_GIVEN,
        expected_total_amount: Any | None | NotGiven = NOT_GIVEN,
        hotel_id: UUID,
        oop_reason: str | None | NotGiven = NOT_GIVEN,
        rate_id: UUID,
        rationale: str,
        reason: str | None | NotGiven = NOT_GIVEN,
        request_new_fund: bool | NotGiven = NOT_GIVEN,
        selection_surface_call_id: str | None | NotGiven = NOT_GIVEN,
        spend_allocation_id: UUID | None | NotGiven = NOT_GIVEN,
        traveler_user_id: UUID | None | NotGiven = NOT_GIVEN,
        trip_id: UUID | None | NotGiven = NOT_GIVEN,
    ) -> HotelBookingResult:
        """Book a selected hotel rate (post_agent_tool_api___submit_hotel_booking)."""
        return cast(
            HotelBookingResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-hotel-booking",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "confirm": confirm,
                        "expected_total_amount": expected_total_amount,
                        "hotel_id": hotel_id,
                        "oop_reason": oop_reason,
                        "rate_id": rate_id,
                        "rationale": rationale,
                        "reason": reason,
                        "request_new_fund": request_new_fund,
                        "selection_surface_call_id": selection_surface_call_id,
                        "spend_allocation_id": spend_allocation_id,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOK_HOTEL_METADATA,
            ),
        )

    async def booking_details(
        self,
        *,
        booking_id: UUID,
        rationale: str,
    ) -> BookingDetails:
        """Get itinerary, stay, or rental details plus request status, amount, payment timing, cancellation state, associated spend, error, and approval information for one exact UUID from GetBookings (post_agent_tool_api___get_booking_details)."""
        return cast(
            BookingDetails,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-booking-details",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"booking_id": booking_id, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOKING_DETAILS_METADATA,
            ),
        )

    async def bookings(
        self,
        *,
        booking_reference: str | None | NotGiven = NOT_GIVEN,
        city: str | None | NotGiven = NOT_GIVEN,
        flight_airline: str | None | NotGiven = NOT_GIVEN,
        flight_number: str | None | NotGiven = NOT_GIVEN,
        hotel_name: str | None | NotGiven = NOT_GIVEN,
        include_cars: bool | NotGiven = NOT_GIVEN,
        include_failed: bool | NotGiven = NOT_GIVEN,
        include_flights: bool | NotGiven = NOT_GIVEN,
        include_hotels: bool | NotGiven = NOT_GIVEN,
        include_past: bool | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
        travel_date: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        verification_mode: bool | NotGiven = NOT_GIVEN,
    ) -> BookingsResult:
        """Retrieve flight, hotel, and car rental booking summaries for the user (post_agent_tool_api___get_bookings)."""
        return cast(
            BookingsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-bookings",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_reference": booking_reference,
                        "city": city,
                        "flight_airline": flight_airline,
                        "flight_number": flight_number,
                        "hotel_name": hotel_name,
                        "include_cars": include_cars,
                        "include_failed": include_failed,
                        "include_flights": include_flights,
                        "include_hotels": include_hotels,
                        "include_past": include_past,
                        "limit": limit,
                        "rationale": rationale,
                        "travel_date": travel_date,
                        "traveler_user_id": traveler_user_id,
                        "verification_mode": verification_mode,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_BOOKINGS_METADATA,
            ),
        )

    async def cancel_flight(
        self,
        *,
        booking_id: UUID,
        confirm: bool | NotGiven = NOT_GIVEN,
        preview_id: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> FlightCancellationResponse:
        """Preview or confirm cancellation of an existing flight booking (post_agent_tool_api___submit_flight_cancellation)."""
        return cast(
            FlightCancellationResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-flight-cancellation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_id": booking_id,
                        "confirm": confirm,
                        "preview_id": preview_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CANCEL_FLIGHT_METADATA,
            ),
        )

    async def cancel_hotel(
        self,
        *,
        booking_id: UUID,
        confirm: bool | NotGiven = NOT_GIVEN,
        preview_id: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> HotelCancellationResponse:
        """Preview or confirm cancellation of an existing hotel booking (post_agent_tool_api___submit_hotel_cancellation)."""
        return cast(
            HotelCancellationResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/submit-hotel-cancellation",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "booking_id": booking_id,
                        "confirm": confirm,
                        "preview_id": preview_id,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CANCEL_HOTEL_METADATA,
            ),
        )

    async def create(
        self,
        *,
        are_trip_dates_from_booking_receipt_or_user_input: bool,
        calendar_timezone: str | None | NotGiven = NOT_GIVEN,
        destinations: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        end_date: Any | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        start_date: Any | None | NotGiven = NOT_GIVEN,
        trip_purpose: str | None | NotGiven = NOT_GIVEN,
    ) -> TripCreationResult:
        """Create a new trip for the acting user (post_agent_tool_api___create_trip)."""
        return cast(
            TripCreationResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-trip",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "are_trip_dates_from_booking_receipt_or_user_input": are_trip_dates_from_booking_receipt_or_user_input,
                        "calendar_timezone": calendar_timezone,
                        "destinations": destinations,
                        "end_date": end_date,
                        "name": name,
                        "rationale": rationale,
                        "start_date": start_date,
                        "trip_purpose": trip_purpose,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_CREATE_METADATA,
            ),
        )

    async def hotel_rates(
        self,
        *,
        check_in_date: str,
        check_out_date: str,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        hotel_id: str,
        max_recommended_rates: int | NotGiven = NOT_GIVEN,
        num_adults: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_id: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> GetHotelRatesResult:
        """Fetch available room-rate options for one selected hotel from SearchHotels (post_agent_tool_api___get_hotel_rates)."""
        return cast(
            GetHotelRatesResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-hotel-rates",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "filters": filters,
                        "hotel_id": hotel_id,
                        "max_recommended_rates": max_recommended_rates,
                        "num_adults": num_adults,
                        "rationale": rationale,
                        "search_id": search_id,
                        "traveler_user_id": traveler_user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_HOTEL_RATES_METADATA,
            ),
        )

    async def list(
        self,
        *,
        cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | None | NotGiven = NOT_GIVEN,
        rationale: str,
        status: str | None | NotGiven = NOT_GIVEN,
    ) -> TripListResult:
        """Fetch trips for the acting user with optional filters (post_agent_tool_api___get_user_trips)."""
        return cast(
            TripListResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-user-trips",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "cursor": cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                        "status": status,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LIST_METADATA,
            ),
        )

    async def locations(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        location_type: str | NotGiven = NOT_GIVEN,
        query: str,
        rationale: str,
    ) -> FlightLocationSearchResult:
        """Resolves locations (airports/cities) available for booking a flight from user intent (post_agent_tool_api___get_flight_booking_locations)."""
        return cast(
            FlightLocationSearchResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-flight-booking-locations",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "limit": limit,
                        "location_type": location_type,
                        "query": query,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOCATIONS_METADATA,
            ),
        )

    async def loyalty_program_remove(
        self,
        *,
        rationale: str,
        traveler_loyalty_program_id: str,
    ) -> RemoveTravelerLoyaltyProgramResult:
        """Remove a saved loyalty program from the user's traveler profile (post_agent_tool_api___remove_traveler_loyalty_program)."""
        return cast(
            RemoveTravelerLoyaltyProgramResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/remove-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "rationale": rationale,
                        "traveler_loyalty_program_id": traveler_loyalty_program_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_REMOVE_METADATA,
            ),
        )

    async def loyalty_program_set(
        self,
        *,
        loyalty_number: str,
        program_name: str,
        rationale: str,
    ) -> SetTravelerLoyaltyProgramResult:
        """Set one loyalty program on the user's traveler profile by program name and loyalty number (post_agent_tool_api___set_traveler_loyalty_program)."""
        return cast(
            SetTravelerLoyaltyProgramResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/set-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "program_name": program_name,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAM_SET_METADATA,
            ),
        )

    async def loyalty_programs(
        self,
        *,
        rationale: str,
    ) -> ListTravelerLoyaltyProgramsResult:
        """List saved loyalty programs from the user's traveler profile (post_agent_tool_api___list_traveler_loyalty_programs)."""
        return cast(
            ListTravelerLoyaltyProgramsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-traveler-loyalty-programs",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_LOYALTY_PROGRAMS_METADATA,
            ),
        )

    async def offices(
        self,
        *,
        rationale: str,
    ) -> GetOfficeLocationsResult:
        """Retrieve the company's office locations and addresses (post_agent_tool_api___get_office_locations)."""
        return cast(
            GetOfficeLocationsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-office-locations",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_OFFICES_METADATA,
            ),
        )

    async def pending(
        self,
        *,
        next_page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> TravelRequestListResult:
        """Retrieves travel/booking requests that are pending approval from the current user (post_agent_tool_api___get_pending_travel_requests)."""
        return cast(
            TravelRequestListResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-pending-travel-requests",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "next_page_cursor": next_page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PENDING_METADATA,
            ),
        )

    async def profile(
        self,
        *,
        rationale: str,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> GetTravelerProfileResult:
        """Retrieve traveler profile information including name, email, phone, date of birth, gender, known traveler number (KTN/TSA), redress number, and loyalty programs (post_agent_tool_api___get_traveler_profile)."""
        return cast(
            GetTravelerProfileResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-traveler-profile",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"rationale": rationale, "traveler_user_id": traveler_user_id}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PROFILE_METADATA,
            ),
        )

    async def profile_update(
        self,
        *,
        avoid_red_eye_flights: bool | NotGiven = NOT_GIVEN,
        date_of_birth: str | None | NotGiven = NOT_GIVEN,
        email: str | None | NotGiven = NOT_GIVEN,
        first_name: str | None | NotGiven = NOT_GIVEN,
        home_airport_code: str | None | NotGiven = NOT_GIVEN,
        id_gender: str | None | NotGiven = NOT_GIVEN,
        known_traveler_number: str | None | NotGiven = NOT_GIVEN,
        last_name: str | None | NotGiven = NOT_GIVEN,
        loyalty_programs: Sequence[dict[str, Any]] | None | NotGiven = NOT_GIVEN,
        max_stops: int | None | NotGiven = NOT_GIVEN,
        middle_name: str | None | NotGiven = NOT_GIVEN,
        name_prefix: str | None | NotGiven = NOT_GIVEN,
        name_suffix: str | None | NotGiven = NOT_GIVEN,
        phone_country_code: str | None | NotGiven = NOT_GIVEN,
        phone_number: str | None | NotGiven = NOT_GIVEN,
        preferred_airlines: Sequence[str] | NotGiven = NOT_GIVEN,
        preferred_arrival_time_window: str | None | NotGiven = NOT_GIVEN,
        preferred_cabin_class: str | None | NotGiven = NOT_GIVEN,
        preferred_departure_time_window: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        redress_number: str | None | NotGiven = NOT_GIVEN,
        seat_preference: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> UpdateTravelerProfileResult:
        """Update traveler identity and contact profile details (post_agent_tool_api___update_traveler_profile)."""
        return cast(
            UpdateTravelerProfileResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-traveler-profile",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "avoid_red_eye_flights": avoid_red_eye_flights,
                        "date_of_birth": date_of_birth,
                        "email": email,
                        "first_name": first_name,
                        "home_airport_code": home_airport_code,
                        "id_gender": id_gender,
                        "known_traveler_number": known_traveler_number,
                        "last_name": last_name,
                        "loyalty_programs": loyalty_programs,
                        "max_stops": max_stops,
                        "middle_name": middle_name,
                        "name_prefix": name_prefix,
                        "name_suffix": name_suffix,
                        "phone_country_code": phone_country_code,
                        "phone_number": phone_number,
                        "preferred_airlines": preferred_airlines,
                        "preferred_arrival_time_window": preferred_arrival_time_window,
                        "preferred_cabin_class": preferred_cabin_class,
                        "preferred_departure_time_window": preferred_departure_time_window,
                        "rationale": rationale,
                        "redress_number": redress_number,
                        "seat_preference": seat_preference,
                        "traveler_user_id": traveler_user_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_PROFILE_UPDATE_METADATA,
            ),
        )

    async def search_flight(
        self,
        *,
        airlines: Sequence[str] | None | NotGiven = NOT_GIVEN,
        arrival: str | None | NotGiven = NOT_GIVEN,
        avoid_red_eye_flights: bool | None | NotGiven = NOT_GIVEN,
        cabin_class: Any | None | NotGiven = NOT_GIVEN,
        clear_preferences: Sequence[str] | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        departure: str | None | NotGiven = NOT_GIVEN,
        departure_date: str | None | NotGiven = NOT_GIVEN,
        include_fare_options: bool | NotGiven = NOT_GIVEN,
        job_id: str | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_stops: int | None | NotGiven = NOT_GIVEN,
        only_split_tickets: bool | None | NotGiven = NOT_GIVEN,
        outbound_offer_id: str | None | NotGiven = NOT_GIVEN,
        preferred_arrival_time_window: str | None | NotGiven = NOT_GIVEN,
        preferred_departure_time_window: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        requested_weekday: str | None | NotGiven = NOT_GIVEN,
        return_date: str | None | NotGiven = NOT_GIVEN,
        sort_key: str | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        trip_id: str | None | NotGiven = NOT_GIVEN,
        wait_for_results: bool | NotGiven = NOT_GIVEN,
    ) -> SearchFlightsResult:
        """Search for flights and return policy-tagged offers ready to quote (post_agent_tool_api___search_flights)."""
        return cast(
            SearchFlightsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-flights",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "airlines": airlines,
                        "arrival": arrival,
                        "avoid_red_eye_flights": avoid_red_eye_flights,
                        "cabin_class": cabin_class,
                        "clear_preferences": clear_preferences,
                        "cursor": cursor,
                        "departure": departure,
                        "departure_date": departure_date,
                        "include_fare_options": include_fare_options,
                        "job_id": job_id,
                        "limit": limit,
                        "max_stops": max_stops,
                        "only_split_tickets": only_split_tickets,
                        "outbound_offer_id": outbound_offer_id,
                        "preferred_arrival_time_window": preferred_arrival_time_window,
                        "preferred_departure_time_window": preferred_departure_time_window,
                        "rationale": rationale,
                        "requested_weekday": requested_weekday,
                        "return_date": return_date,
                        "sort_key": sort_key,
                        "traveler_user_id": traveler_user_id,
                        "trip_id": trip_id,
                        "wait_for_results": wait_for_results,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_SEARCH_FLIGHT_METADATA,
            ),
        )

    async def search_hotel(
        self,
        *,
        check_in_date: str | None | NotGiven = NOT_GIVEN,
        check_out_date: str | None | NotGiven = NOT_GIVEN,
        cursor: str | None | NotGiven = NOT_GIVEN,
        filters: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        hotel_name: str | None | NotGiven = NOT_GIVEN,
        latitude: Any | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location_query: str | None | NotGiven = NOT_GIVEN,
        longitude: Any | None | NotGiven = NOT_GIVEN,
        num_adults: int | NotGiven = NOT_GIVEN,
        preferences: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        search_id: str | None | NotGiven = NOT_GIVEN,
        sort: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        traveler_user_id: str | None | NotGiven = NOT_GIVEN,
        wait_for_results: bool | None | NotGiven = NOT_GIVEN,
    ) -> SearchHotelsResult:
        """Search hotels using the canonical Ramp web inventory and policy flow (post_agent_tool_api___search_hotels)."""
        return cast(
            SearchHotelsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-hotel",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "check_in_date": check_in_date,
                        "check_out_date": check_out_date,
                        "cursor": cursor,
                        "filters": filters,
                        "hotel_name": hotel_name,
                        "latitude": latitude,
                        "limit": limit,
                        "location_query": location_query,
                        "longitude": longitude,
                        "num_adults": num_adults,
                        "preferences": preferences,
                        "rationale": rationale,
                        "search_id": search_id,
                        "sort": sort,
                        "traveler_user_id": traveler_user_id,
                        "wait_for_results": wait_for_results,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_SEARCH_HOTEL_METADATA,
            ),
        )

    async def update_traveler_loyalty_program(
        self,
        *,
        loyalty_number: str,
        rationale: str,
        traveler_loyalty_program_id: str,
    ) -> TravelerLoyaltyProgramCompatibilityResult:
        """Compatibility route for callers that still update a saved loyalty program by ID (post_agent_tool_api___traveler_loyalty_program_number_setter)."""
        return cast(
            TravelerLoyaltyProgramCompatibilityResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/update-traveler-loyalty-program",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "loyalty_number": loyalty_number,
                        "rationale": rationale,
                        "traveler_loyalty_program_id": traveler_loyalty_program_id,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TRAVEL_UPDATE_TRAVELER_LOYALTY_PROGRAM_METADATA,
            ),
        )


class AgentToolsTreasury:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def accounts(
        self,
        *,
        rationale: str,
    ) -> ListBusinessAccountsOutput:
        """List all Ramp Checking Accounts (wallet accounts) for the user's business (get_agent_tool_api___list_business_accounts)."""
        return cast(
            ListBusinessAccountsOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-business-accounts",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_ACCOUNTS_METADATA,
            ),
        )

    def balance_history(
        self,
        *,
        account_uuid: str,
        end_date: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        start_date: str | None | NotGiven = NOT_GIVEN,
    ) -> GetAccountBalanceHistoryOutput:
        """Get daily balance history for a specific Ramp Checking Account (get_agent_tool_api___get_account_balance_history)."""
        return cast(
            GetAccountBalanceHistoryOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-account-balance-history",
                path_params=None,
                params=_without_not_given(
                    {
                        "account_uuid": account_uuid,
                        "end_date": end_date,
                        "rationale": rationale,
                        "start_date": start_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_BALANCE_HISTORY_METADATA,
            ),
        )

    def history(
        self,
        *,
        end_date: str,
        rationale: str,
        start_date: str,
    ) -> GetTreasuryBalanceHistoryOutput:
        """Get daily balance history across all Treasury accounts for a date range (get_agent_tool_api___get_treasury_balance_history)."""
        return cast(
            GetTreasuryBalanceHistoryOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-treasury-balance-history",
                path_params=None,
                params=_without_not_given(
                    {
                        "end_date": end_date,
                        "rationale": rationale,
                        "start_date": start_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_HISTORY_METADATA,
            ),
        )

    def investments(
        self,
        *,
        rationale: str,
    ) -> GetInvestmentAccountBalanceOutput:
        """Get the balance of investment accounts for the business (get_agent_tool_api___get_investment_account_balance)."""
        return cast(
            GetInvestmentAccountBalanceOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-investment-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_INVESTMENTS_METADATA,
            ),
        )

    def list(
        self,
        *,
        rationale: str,
    ) -> ListTreasuryAccountsOutput:
        """List all Treasury accounts (Ramp Checking Accounts, Investment Accounts, Managed Portfolios) (get_agent_tool_api___list_treasury_accounts)."""
        return cast(
            ListTreasuryAccountsOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-treasury-accounts",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_LIST_METADATA,
            ),
        )

    def portfolio(
        self,
        *,
        rationale: str,
    ) -> GetManagedPortfolioAccountBalanceOutput:
        """Get the balance of managed portfolio accounts for the business (get_agent_tool_api___get_managed_portfolio_account_balance)."""
        return cast(
            GetManagedPortfolioAccountBalanceOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-managed-portfolio-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_PORTFOLIO_METADATA,
            ),
        )

    def summary(
        self,
        *,
        rationale: str,
    ) -> GetRampBusinessAccountBalanceOutput:
        """Get the balance of Ramp Checking Accounts for the business (get_agent_tool_api___get_ramp_business_account_balance)."""
        return cast(
            GetRampBusinessAccountBalanceOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-ramp-business-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_SUMMARY_METADATA,
            ),
        )

    def transfers(
        self,
        *,
        cursor: UUID | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> ListWalletTransfersOutput:
        """List wallet transfers for the user's business Ramp Checking Accounts (get_agent_tool_api___list_wallet_transfers)."""
        return cast(
            ListWalletTransfersOutput,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-wallet-transfers",
                path_params=None,
                params=_without_not_given(
                    {
                        "cursor": cursor,
                        "from_date": from_date,
                        "page_size": page_size,
                        "rationale": rationale,
                        "to_date": to_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_TRANSFERS_METADATA,
            ),
        )


class AsyncAgentToolsTreasury:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def accounts(
        self,
        *,
        rationale: str,
    ) -> ListBusinessAccountsOutput:
        """List all Ramp Checking Accounts (wallet accounts) for the user's business (get_agent_tool_api___list_business_accounts)."""
        return cast(
            ListBusinessAccountsOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-business-accounts",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_ACCOUNTS_METADATA,
            ),
        )

    async def balance_history(
        self,
        *,
        account_uuid: str,
        end_date: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        start_date: str | None | NotGiven = NOT_GIVEN,
    ) -> GetAccountBalanceHistoryOutput:
        """Get daily balance history for a specific Ramp Checking Account (get_agent_tool_api___get_account_balance_history)."""
        return cast(
            GetAccountBalanceHistoryOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-account-balance-history",
                path_params=None,
                params=_without_not_given(
                    {
                        "account_uuid": account_uuid,
                        "end_date": end_date,
                        "rationale": rationale,
                        "start_date": start_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_BALANCE_HISTORY_METADATA,
            ),
        )

    async def history(
        self,
        *,
        end_date: str,
        rationale: str,
        start_date: str,
    ) -> GetTreasuryBalanceHistoryOutput:
        """Get daily balance history across all Treasury accounts for a date range (get_agent_tool_api___get_treasury_balance_history)."""
        return cast(
            GetTreasuryBalanceHistoryOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-treasury-balance-history",
                path_params=None,
                params=_without_not_given(
                    {
                        "end_date": end_date,
                        "rationale": rationale,
                        "start_date": start_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_HISTORY_METADATA,
            ),
        )

    async def investments(
        self,
        *,
        rationale: str,
    ) -> GetInvestmentAccountBalanceOutput:
        """Get the balance of investment accounts for the business (get_agent_tool_api___get_investment_account_balance)."""
        return cast(
            GetInvestmentAccountBalanceOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-investment-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_INVESTMENTS_METADATA,
            ),
        )

    async def list(
        self,
        *,
        rationale: str,
    ) -> ListTreasuryAccountsOutput:
        """List all Treasury accounts (Ramp Checking Accounts, Investment Accounts, Managed Portfolios) (get_agent_tool_api___list_treasury_accounts)."""
        return cast(
            ListTreasuryAccountsOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-treasury-accounts",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_LIST_METADATA,
            ),
        )

    async def portfolio(
        self,
        *,
        rationale: str,
    ) -> GetManagedPortfolioAccountBalanceOutput:
        """Get the balance of managed portfolio accounts for the business (get_agent_tool_api___get_managed_portfolio_account_balance)."""
        return cast(
            GetManagedPortfolioAccountBalanceOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-managed-portfolio-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_PORTFOLIO_METADATA,
            ),
        )

    async def summary(
        self,
        *,
        rationale: str,
    ) -> GetRampBusinessAccountBalanceOutput:
        """Get the balance of Ramp Checking Accounts for the business (get_agent_tool_api___get_ramp_business_account_balance)."""
        return cast(
            GetRampBusinessAccountBalanceOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-ramp-business-account-balance",
                path_params=None,
                params=_without_not_given({"rationale": rationale}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_SUMMARY_METADATA,
            ),
        )

    async def transfers(
        self,
        *,
        cursor: UUID | None | NotGiven = NOT_GIVEN,
        from_date: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
        to_date: str | None | NotGiven = NOT_GIVEN,
    ) -> ListWalletTransfersOutput:
        """List wallet transfers for the user's business Ramp Checking Accounts (get_agent_tool_api___list_wallet_transfers)."""
        return cast(
            ListWalletTransfersOutput,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/list-wallet-transfers",
                path_params=None,
                params=_without_not_given(
                    {
                        "cursor": cursor,
                        "from_date": from_date,
                        "page_size": page_size,
                        "rationale": rationale,
                        "to_date": to_date,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_TREASURY_TRANSFERS_METADATA,
            ),
        )


class AgentToolsUsers:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(
        self,
        *,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        name_search: str | None | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> GetAllReducedUsersResult:
        """List and search users across the entire business (post_agent_tool_api___get_all_reduced_users)."""
        return cast(
            GetAllReducedUsersResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-users",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_ids": department_ids,
                        "location_ids": location_ids,
                        "name_search": name_search,
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_LIST_METADATA,
            ),
        )

    def me(
        self,
        *,
        rationale: str,
    ) -> SimplifiedUserDetailResponse:
        """Get the current user's details (post_agent_tool_api___get_simplified_user_detail)."""
        return cast(
            SimplifiedUserDetailResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-simplified-user-detail",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_ME_METADATA,
            ),
        )

    def org_chart(
        self,
        *,
        rationale: str,
        user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> OrgChartResponse:
        """Get org chart for a user, including reporting chain and direct reports (post_agent_tool_api___get_org_chart)."""
        return cast(
            OrgChartResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-org-chart",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "user_id": user_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_ORG_CHART_METADATA,
            ),
        )


class AsyncAgentToolsUsers:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self,
        *,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        location_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        name_search: str | None | NotGiven = NOT_GIVEN,
        page_cursor: str | None | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> GetAllReducedUsersResult:
        """List and search users across the entire business (post_agent_tool_api___get_all_reduced_users)."""
        return cast(
            GetAllReducedUsersResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-users",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "department_ids": department_ids,
                        "location_ids": location_ids,
                        "name_search": name_search,
                        "page_cursor": page_cursor,
                        "page_size": page_size,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_LIST_METADATA,
            ),
        )

    async def me(
        self,
        *,
        rationale: str,
    ) -> SimplifiedUserDetailResponse:
        """Get the current user's details (post_agent_tool_api___get_simplified_user_detail)."""
        return cast(
            SimplifiedUserDetailResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-simplified-user-detail",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_ME_METADATA,
            ),
        )

    async def org_chart(
        self,
        *,
        rationale: str,
        user_id: str | None | NotGiven = NOT_GIVEN,
    ) -> OrgChartResponse:
        """Get org chart for a user, including reporting chain and direct reports (post_agent_tool_api___get_org_chart)."""
        return cast(
            OrgChartResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-org-chart",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given({"rationale": rationale, "user_id": user_id}),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_USERS_ORG_CHART_METADATA,
            ),
        )


class AgentToolsVendors:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def attach_document(
        self,
        *,
        content_type: str,
        document_category: str,
        file_content_base64: str,
        filename: str,
        rationale: str,
        vendor_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> AttachVendorDocumentResult:
        """Attach a vendor document from base64-encoded file content (post_agent_tool_api___attach_vendor_document)."""
        return cast(
            AttachVendorDocumentResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/attach-vendor-document",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "content_type": content_type,
                        "document_category": document_category,
                        "file_content_base64": file_content_base64,
                        "filename": filename,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_ATTACH_DOCUMENT_METADATA,
            ),
        )

    def bulk_upload(
        self,
        *,
        documents: Sequence[dict[str, Any]],
        rationale: str,
        vendor_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> BulkUploadVendorDocumentsResult:
        """Bulk upload vendor documents from base64-encoded file content (post_agent_tool_api___bulk_upload_vendor_documents)."""
        return cast(
            BulkUploadVendorDocumentsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/bulk-upload-vendor-documents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "documents": documents,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_BULK_UPLOAD_METADATA,
            ),
        )

    def bulk_upload_status(
        self,
        *,
        batch_id: str,
        is_w_document: bool | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> GetVendorDocumentBulkStatusResult:
        """Get bulk vendor document upload progress and current document review state (get_agent_tool_api___get_vendor_document_bulk_status)."""
        return cast(
            GetVendorDocumentBulkStatusResult,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-vendor-document-bulk-status",
                path_params=None,
                params=_without_not_given(
                    {
                        "batch_id": batch_id,
                        "is_w_document": is_w_document,
                        "rationale": rationale,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_BULK_UPLOAD_STATUS_METADATA,
            ),
        )

    def create(
        self,
        *,
        contact: dict[str, Any],
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        website: str | None | NotGiven = NOT_GIVEN,
    ) -> CreateDraftPayeeResult:
        """Create a pending vendor/payee record (post_agent_tool_api___create_pending_payee_direct)."""
        return cast(
            CreateDraftPayeeResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-pending-payee",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "contact": contact,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "website": website,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_CREATE_METADATA,
            ),
        )

    def get(
        self,
        *,
        payee_agreement_uuid: str,
        rationale: str,
    ) -> GetVendorAgreementPublicResult:
        """Retrieve details for a specific vendor agreement/contract by UUID (post_agent_tool_api___get_vendor_agreement)."""
        return cast(
            GetVendorAgreementPublicResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-vendor-agreement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_agreement_uuid": payee_agreement_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_GET_METADATA,
            ),
        )

    def list(
        self,
        *,
        auto_renews: bool | None | NotGiven = NOT_GIVEN,
        contract_owner_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        has_end_date: bool | None | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        is_active: bool | None | NotGiven = NOT_GIVEN,
        is_up_for_renewal: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_days_remaining: int | None | NotGiven = NOT_GIVEN,
        max_end_date: str | None | NotGiven = NOT_GIVEN,
        max_last_date_to_terminate: str | None | NotGiven = NOT_GIVEN,
        max_start_date: str | None | NotGiven = NOT_GIVEN,
        max_total_value: Any | None | NotGiven = NOT_GIVEN,
        min_days_remaining: int | None | NotGiven = NOT_GIVEN,
        min_end_date: str | None | NotGiven = NOT_GIVEN,
        min_last_date_to_terminate: str | None | NotGiven = NOT_GIVEN,
        min_start_date: str | None | NotGiven = NOT_GIVEN,
        min_total_value: Any | None | NotGiven = NOT_GIVEN,
        payee_agreement_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        payee_owner_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        payee_uuid: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        renewal_status: Sequence[str] | None | NotGiven = NOT_GIVEN,
        sort_ascending: bool | None | NotGiven = NOT_GIVEN,
        sort_by: str | None | NotGiven = NOT_GIVEN,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> ListVendorAgreementsResult:
        """List and filter vendor agreements/contracts across the business (post_agent_tool_api___list_vendor_agreements)."""
        return cast(
            ListVendorAgreementsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-vendor-agreements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "auto_renews": auto_renews,
                        "contract_owner_ids": contract_owner_ids,
                        "department_ids": department_ids,
                        "has_end_date": has_end_date,
                        "include_archived": include_archived,
                        "is_active": is_active,
                        "is_up_for_renewal": is_up_for_renewal,
                        "limit": limit,
                        "max_days_remaining": max_days_remaining,
                        "max_end_date": max_end_date,
                        "max_last_date_to_terminate": max_last_date_to_terminate,
                        "max_start_date": max_start_date,
                        "max_total_value": max_total_value,
                        "min_days_remaining": min_days_remaining,
                        "min_end_date": min_end_date,
                        "min_last_date_to_terminate": min_last_date_to_terminate,
                        "min_start_date": min_start_date,
                        "min_total_value": min_total_value,
                        "payee_agreement_ids": payee_agreement_ids,
                        "payee_owner_ids": payee_owner_ids,
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "renewal_status": renewal_status,
                        "sort_ascending": sort_ascending,
                        "sort_by": sort_by,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_LIST_METADATA,
            ),
        )

    def search(
        self,
        *,
        include_draft: bool | NotGiven = NOT_GIVEN,
        is_1099_tracking_enabled: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_term: str | None | NotGiven = NOT_GIVEN,
        tax_1099_year: int | None | NotGiven = NOT_GIVEN,
    ) -> SearchVendorsResult:
        """Search for vendors (payees) within the business by name (post_agent_tool_api___search_vendors)."""
        return cast(
            SearchVendorsResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-vendors",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_draft": include_draft,
                        "is_1099_tracking_enabled": is_1099_tracking_enabled,
                        "limit": limit,
                        "rationale": rationale,
                        "search_term": search_term,
                        "tax_1099_year": tax_1099_year,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_SEARCH_METADATA,
            ),
        )


class AsyncAgentToolsVendors:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def attach_document(
        self,
        *,
        content_type: str,
        document_category: str,
        file_content_base64: str,
        filename: str,
        rationale: str,
        vendor_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> AttachVendorDocumentResult:
        """Attach a vendor document from base64-encoded file content (post_agent_tool_api___attach_vendor_document)."""
        return cast(
            AttachVendorDocumentResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/attach-vendor-document",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "content_type": content_type,
                        "document_category": document_category,
                        "file_content_base64": file_content_base64,
                        "filename": filename,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_ATTACH_DOCUMENT_METADATA,
            ),
        )

    async def bulk_upload(
        self,
        *,
        documents: Sequence[dict[str, Any]],
        rationale: str,
        vendor_uuid: str | None | NotGiven = NOT_GIVEN,
    ) -> BulkUploadVendorDocumentsResult:
        """Bulk upload vendor documents from base64-encoded file content (post_agent_tool_api___bulk_upload_vendor_documents)."""
        return cast(
            BulkUploadVendorDocumentsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/bulk-upload-vendor-documents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "documents": documents,
                        "rationale": rationale,
                        "vendor_uuid": vendor_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_BULK_UPLOAD_METADATA,
            ),
        )

    async def bulk_upload_status(
        self,
        *,
        batch_id: str,
        is_w_document: bool | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> GetVendorDocumentBulkStatusResult:
        """Get bulk vendor document upload progress and current document review state (get_agent_tool_api___get_vendor_document_bulk_status)."""
        return cast(
            GetVendorDocumentBulkStatusResult,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-tools/get-vendor-document-bulk-status",
                path_params=None,
                params=_without_not_given(
                    {
                        "batch_id": batch_id,
                        "is_w_document": is_w_document,
                        "rationale": rationale,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_BULK_UPLOAD_STATUS_METADATA,
            ),
        )

    async def create(
        self,
        *,
        contact: dict[str, Any],
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        rationale: str,
        website: str | None | NotGiven = NOT_GIVEN,
    ) -> CreateDraftPayeeResult:
        """Create a pending vendor/payee record (post_agent_tool_api___create_pending_payee_direct)."""
        return cast(
            CreateDraftPayeeResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/create-pending-payee",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "contact": contact,
                        "description": description,
                        "name": name,
                        "rationale": rationale,
                        "website": website,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_CREATE_METADATA,
            ),
        )

    async def get(
        self,
        *,
        payee_agreement_uuid: str,
        rationale: str,
    ) -> GetVendorAgreementPublicResult:
        """Retrieve details for a specific vendor agreement/contract by UUID (post_agent_tool_api___get_vendor_agreement)."""
        return cast(
            GetVendorAgreementPublicResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/get-vendor-agreement",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "payee_agreement_uuid": payee_agreement_uuid,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_GET_METADATA,
            ),
        )

    async def list(
        self,
        *,
        auto_renews: bool | None | NotGiven = NOT_GIVEN,
        contract_owner_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        department_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        has_end_date: bool | None | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        is_active: bool | None | NotGiven = NOT_GIVEN,
        is_up_for_renewal: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        max_days_remaining: int | None | NotGiven = NOT_GIVEN,
        max_end_date: str | None | NotGiven = NOT_GIVEN,
        max_last_date_to_terminate: str | None | NotGiven = NOT_GIVEN,
        max_start_date: str | None | NotGiven = NOT_GIVEN,
        max_total_value: Any | None | NotGiven = NOT_GIVEN,
        min_days_remaining: int | None | NotGiven = NOT_GIVEN,
        min_end_date: str | None | NotGiven = NOT_GIVEN,
        min_last_date_to_terminate: str | None | NotGiven = NOT_GIVEN,
        min_start_date: str | None | NotGiven = NOT_GIVEN,
        min_total_value: Any | None | NotGiven = NOT_GIVEN,
        payee_agreement_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        payee_owner_ids: Sequence[str] | None | NotGiven = NOT_GIVEN,
        payee_uuid: str | None | NotGiven = NOT_GIVEN,
        rationale: str,
        renewal_status: Sequence[str] | None | NotGiven = NOT_GIVEN,
        sort_ascending: bool | None | NotGiven = NOT_GIVEN,
        sort_by: str | None | NotGiven = NOT_GIVEN,
        vendor_name: str | None | NotGiven = NOT_GIVEN,
    ) -> ListVendorAgreementsResult:
        """List and filter vendor agreements/contracts across the business (post_agent_tool_api___list_vendor_agreements)."""
        return cast(
            ListVendorAgreementsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/list-vendor-agreements",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "auto_renews": auto_renews,
                        "contract_owner_ids": contract_owner_ids,
                        "department_ids": department_ids,
                        "has_end_date": has_end_date,
                        "include_archived": include_archived,
                        "is_active": is_active,
                        "is_up_for_renewal": is_up_for_renewal,
                        "limit": limit,
                        "max_days_remaining": max_days_remaining,
                        "max_end_date": max_end_date,
                        "max_last_date_to_terminate": max_last_date_to_terminate,
                        "max_start_date": max_start_date,
                        "max_total_value": max_total_value,
                        "min_days_remaining": min_days_remaining,
                        "min_end_date": min_end_date,
                        "min_last_date_to_terminate": min_last_date_to_terminate,
                        "min_start_date": min_start_date,
                        "min_total_value": min_total_value,
                        "payee_agreement_ids": payee_agreement_ids,
                        "payee_owner_ids": payee_owner_ids,
                        "payee_uuid": payee_uuid,
                        "rationale": rationale,
                        "renewal_status": renewal_status,
                        "sort_ascending": sort_ascending,
                        "sort_by": sort_by,
                        "vendor_name": vendor_name,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_LIST_METADATA,
            ),
        )

    async def search(
        self,
        *,
        include_draft: bool | NotGiven = NOT_GIVEN,
        is_1099_tracking_enabled: bool | None | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        rationale: str,
        search_term: str | None | NotGiven = NOT_GIVEN,
        tax_1099_year: int | None | NotGiven = NOT_GIVEN,
    ) -> SearchVendorsResult:
        """Search for vendors (payees) within the business by name (post_agent_tool_api___search_vendors)."""
        return cast(
            SearchVendorsResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/search-vendors",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "include_draft": include_draft,
                        "is_1099_tracking_enabled": is_1099_tracking_enabled,
                        "limit": limit,
                        "rationale": rationale,
                        "search_term": search_term,
                        "tax_1099_year": tax_1099_year,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_VENDORS_SEARCH_METADATA,
            ),
        )


class AgentToolsX402:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        confirmed: bool,
        rationale: str,
    ) -> X402WalletReady:
        """Provision your business's x402 wallet after the user explicitly confirms (post_agent_tool_api___provision_x402_wallet)."""
        return cast(
            X402WalletReady,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/provision-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"confirmed": confirmed, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_CREATE_METADATA,
            ),
        )

    def fund(
        self,
        *,
        amount: Any,
        idempotency_key: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        source_wallet_account_uuid: UUID,
    ) -> FundX402WalletResult:
        """Fund the business's x402 wallet from a Ramp Checking Account (post_agent_tool_api___fund_x402_wallet)."""
        return cast(
            FundX402WalletResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/fund-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                        "source_wallet_account_uuid": source_wallet_account_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_FUND_METADATA,
            ),
        )

    def pay(
        self,
        *,
        accepted: dict[str, Any],
        extensions: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        idempotency_key: UUID,
        rationale: str,
        resource: dict[str, Any],
    ) -> X402PaymentSigned:
        """Pay an x402 payment request from your business's stablecoin balance (post_agent_tool_api___pay_with_x402)."""
        return cast(
            X402PaymentSigned,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/pay-with-x402",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accepted": accepted,
                        "extensions": extensions,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                        "resource": resource,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_PAY_METADATA,
            ),
        )

    def withdraw(
        self,
        *,
        amount: Any,
        destination_wallet_account_uuid: UUID,
        idempotency_key: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> WithdrawX402WalletResult:
        """Withdraw the business's x402 wallet balance to a Ramp Checking Account (post_agent_tool_api___withdraw_x402_wallet)."""
        return cast(
            WithdrawX402WalletResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/withdraw-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "destination_wallet_account_uuid": destination_wallet_account_uuid,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_WITHDRAW_METADATA,
            ),
        )


class AsyncAgentToolsX402:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        confirmed: bool,
        rationale: str,
    ) -> X402WalletReady:
        """Provision your business's x402 wallet after the user explicitly confirms (post_agent_tool_api___provision_x402_wallet)."""
        return cast(
            X402WalletReady,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/provision-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {"confirmed": confirmed, "rationale": rationale}
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_CREATE_METADATA,
            ),
        )

    async def fund(
        self,
        *,
        amount: Any,
        idempotency_key: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
        source_wallet_account_uuid: UUID,
    ) -> FundX402WalletResult:
        """Fund the business's x402 wallet from a Ramp Checking Account (post_agent_tool_api___fund_x402_wallet)."""
        return cast(
            FundX402WalletResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/fund-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                        "source_wallet_account_uuid": source_wallet_account_uuid,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_FUND_METADATA,
            ),
        )

    async def pay(
        self,
        *,
        accepted: dict[str, Any],
        extensions: dict[str, Any] | None | NotGiven = NOT_GIVEN,
        idempotency_key: UUID,
        rationale: str,
        resource: dict[str, Any],
    ) -> X402PaymentSigned:
        """Pay an x402 payment request from your business's stablecoin balance (post_agent_tool_api___pay_with_x402)."""
        return cast(
            X402PaymentSigned,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/pay-with-x402",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "accepted": accepted,
                        "extensions": extensions,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                        "resource": resource,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_PAY_METADATA,
            ),
        )

    async def withdraw(
        self,
        *,
        amount: Any,
        destination_wallet_account_uuid: UUID,
        idempotency_key: UUID | None | NotGiven = NOT_GIVEN,
        rationale: str,
    ) -> WithdrawX402WalletResult:
        """Withdraw the business's x402 wallet balance to a Ramp Checking Account (post_agent_tool_api___withdraw_x402_wallet)."""
        return cast(
            WithdrawX402WalletResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/withdraw-x402-wallet",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "amount": amount,
                        "destination_wallet_account_uuid": destination_wallet_account_uuid,
                        "idempotency_key": idempotency_key,
                        "rationale": rationale,
                    }
                ),
                data=None,
                files=None,
                metadata=_AGENT_TOOLS_X402_WITHDRAW_METADATA,
            ),
        )


class Accounting:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def mark_ready_to_sync(
        self,
        *,
        object_ids: Sequence[UUID],
        object_type: str,
    ) -> None:
        """Mark objects as ready to sync to your accounting provider (post_ready_to_sync_resource)."""
        self._transport.request(
            method="POST",
            path="/developer/v1/accounting/ready-to-sync",
            path_params=None,
            params=None,
            headers=None,
            json=_without_not_given(
                {"object_ids": object_ids, "object_type": object_type}
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_ACCOUNTING_MARK_READY_TO_SYNC_METADATA,
        )
        return None


class AsyncAccounting:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def mark_ready_to_sync(
        self,
        *,
        object_ids: Sequence[UUID],
        object_type: str,
    ) -> None:
        """Mark objects as ready to sync to your accounting provider (post_ready_to_sync_resource)."""
        await self._transport.request(
            method="POST",
            path="/developer/v1/accounting/ready-to-sync",
            path_params=None,
            params=None,
            headers=None,
            json=_without_not_given(
                {"object_ids": object_ids, "object_type": object_type}
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_ACCOUNTING_MARK_READY_TO_SYNC_METADATA,
        )
        return None


class AgentWallet:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(
        self,
        *,
        agent_id: str,
        limit: int | NotGiven = NOT_GIVEN,
    ) -> AgentWalletPolicyListResponse:
        """List policy versions for a standalone Agent Wallet (get_agent_wallet_policy_publication_resource)."""
        return cast(
            AgentWalletPolicyListResponse,
            self._transport.request(
                method="GET",
                path="/developer/v1/agent-wallet/agents/{agent_id}/policies",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=_without_not_given({"limit": limit}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENT_WALLET_LIST_METADATA,
            ),
        )

    def publish_policy(
        self,
        *,
        agent_id: str,
        approval_mode: str | NotGiven = NOT_GIVEN,
        approval_validity_seconds: int | NotGiven = NOT_GIVEN,
        configurations: Sequence[Any],
        constraints: dict[str, Any],
        policy_version: UUID,
        schema_version: int,
    ) -> None:
        """Publish the active policy for a standalone Agent Wallet (post_agent_wallet_policy_publication_resource)."""
        self._transport.request(
            method="POST",
            path="/developer/v1/agent-wallet/agents/{agent_id}/policies",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=_without_not_given(
                {
                    "approval_mode": approval_mode,
                    "approval_validity_seconds": approval_validity_seconds,
                    "configurations": configurations,
                    "constraints": constraints,
                    "policy_version": policy_version,
                    "schema_version": schema_version,
                }
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENT_WALLET_PUBLISH_POLICY_METADATA,
        )
        return None


class AsyncAgentWallet:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self,
        *,
        agent_id: str,
        limit: int | NotGiven = NOT_GIVEN,
    ) -> AgentWalletPolicyListResponse:
        """List policy versions for a standalone Agent Wallet (get_agent_wallet_policy_publication_resource)."""
        return cast(
            AgentWalletPolicyListResponse,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agent-wallet/agents/{agent_id}/policies",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=_without_not_given({"limit": limit}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENT_WALLET_LIST_METADATA,
            ),
        )

    async def publish_policy(
        self,
        *,
        agent_id: str,
        approval_mode: str | NotGiven = NOT_GIVEN,
        approval_validity_seconds: int | NotGiven = NOT_GIVEN,
        configurations: Sequence[Any],
        constraints: dict[str, Any],
        policy_version: UUID,
        schema_version: int,
    ) -> None:
        """Publish the active policy for a standalone Agent Wallet (post_agent_wallet_policy_publication_resource)."""
        await self._transport.request(
            method="POST",
            path="/developer/v1/agent-wallet/agents/{agent_id}/policies",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=_without_not_given(
                {
                    "approval_mode": approval_mode,
                    "approval_validity_seconds": approval_validity_seconds,
                    "configurations": configurations,
                    "constraints": constraints,
                    "policy_version": policy_version,
                    "schema_version": schema_version,
                }
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENT_WALLET_PUBLISH_POLICY_METADATA,
        )
        return None


class Agents:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def create(
        self,
        *,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        owner_id: UUID | None | NotGiven = NOT_GIVEN,
        role_ids: Sequence[UUID],
    ) -> AgentCreateResponse:
        """Create a standalone agent in the authenticated business (post_agent_list_resource)."""
        return cast(
            AgentCreateResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/agents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "description": description,
                        "name": name,
                        "owner_id": owner_id,
                        "role_ids": role_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_CREATE_METADATA,
            ),
        )

    def delete(
        self,
        *,
        agent_id: UUID,
    ) -> None:
        """Soft-delete a standalone agent and revoke its OAuth client (delete_agent_item_resource)."""
        self._transport.request(
            method="DELETE",
            path="/developer/v1/agents/{agent_id}",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=None,
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENTS_DELETE_METADATA,
        )
        return None

    def get(
        self,
        *,
        agent_id: UUID,
    ) -> Agent:
        """Fetch a standalone agent in the authenticated business (get_agent_item_resource)."""
        return cast(
            Agent,
            self._transport.request(
                method="GET",
                path="/developer/v1/agents/{agent_id}",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_GET_METADATA,
            ),
        )

    def list(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseAgentSchema:
        """List active standalone agents in the authenticated business (get_agent_list_resource)."""
        return cast(
            PaginatedResponseAgentSchema,
            self._transport.request(
                method="GET",
                path="/developer/v1/agents",
                path_params=None,
                params=_without_not_given({"page_size": page_size, "start": start}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_LIST_METADATA,
            ),
        )

    def rotate_secret(
        self,
        *,
        agent_id: UUID,
    ) -> AgentCredentials:
        """Rotate a standalone agent's client secret (post_agent_rotate_secret_resource)."""
        return cast(
            AgentCredentials,
            self._transport.request(
                method="POST",
                path="/developer/v1/agents/{agent_id}/secret",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_ROTATE_SECRET_METADATA,
            ),
        )

    def set_status(
        self,
        *,
        agent_id: UUID,
        status: str,
    ) -> None:
        """Deactivate or reactivate a standalone agent (post_agent_status_resource)."""
        self._transport.request(
            method="POST",
            path="/developer/v1/agents/{agent_id}/status",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=_without_not_given({"status": status}),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENTS_SET_STATUS_METADATA,
        )
        return None

    def update(
        self,
        *,
        agent_id: UUID,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner_id: UUID | NotGiven = NOT_GIVEN,
        role_ids: Sequence[UUID] | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """Update a standalone agent's name, description, owner, or custom roles (patch_agent_item_resource)."""
        return cast(
            Agent,
            self._transport.request(
                method="PATCH",
                path="/developer/v1/agents/{agent_id}",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "description": description,
                        "name": name,
                        "owner_id": owner_id,
                        "role_ids": role_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_UPDATE_METADATA,
            ),
        )


class AsyncAgents:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def create(
        self,
        *,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str,
        owner_id: UUID | None | NotGiven = NOT_GIVEN,
        role_ids: Sequence[UUID],
    ) -> AgentCreateResponse:
        """Create a standalone agent in the authenticated business (post_agent_list_resource)."""
        return cast(
            AgentCreateResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agents",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "description": description,
                        "name": name,
                        "owner_id": owner_id,
                        "role_ids": role_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_CREATE_METADATA,
            ),
        )

    async def delete(
        self,
        *,
        agent_id: UUID,
    ) -> None:
        """Soft-delete a standalone agent and revoke its OAuth client (delete_agent_item_resource)."""
        await self._transport.request(
            method="DELETE",
            path="/developer/v1/agents/{agent_id}",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=None,
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENTS_DELETE_METADATA,
        )
        return None

    async def get(
        self,
        *,
        agent_id: UUID,
    ) -> Agent:
        """Fetch a standalone agent in the authenticated business (get_agent_item_resource)."""
        return cast(
            Agent,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agents/{agent_id}",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_GET_METADATA,
            ),
        )

    async def list(
        self,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseAgentSchema:
        """List active standalone agents in the authenticated business (get_agent_list_resource)."""
        return cast(
            PaginatedResponseAgentSchema,
            await self._transport.request(
                method="GET",
                path="/developer/v1/agents",
                path_params=None,
                params=_without_not_given({"page_size": page_size, "start": start}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_LIST_METADATA,
            ),
        )

    async def rotate_secret(
        self,
        *,
        agent_id: UUID,
    ) -> AgentCredentials:
        """Rotate a standalone agent's client secret (post_agent_rotate_secret_resource)."""
        return cast(
            AgentCredentials,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agents/{agent_id}/secret",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_ROTATE_SECRET_METADATA,
            ),
        )

    async def set_status(
        self,
        *,
        agent_id: UUID,
        status: str,
    ) -> None:
        """Deactivate or reactivate a standalone agent (post_agent_status_resource)."""
        await self._transport.request(
            method="POST",
            path="/developer/v1/agents/{agent_id}/status",
            path_params=_without_not_given({"agent_id": agent_id}),
            params=None,
            headers=None,
            json=_without_not_given({"status": status}),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_AGENTS_SET_STATUS_METADATA,
        )
        return None

    async def update(
        self,
        *,
        agent_id: UUID,
        description: str | None | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner_id: UUID | NotGiven = NOT_GIVEN,
        role_ids: Sequence[UUID] | NotGiven = NOT_GIVEN,
    ) -> Agent:
        """Update a standalone agent's name, description, owner, or custom roles (patch_agent_item_resource)."""
        return cast(
            Agent,
            await self._transport.request(
                method="PATCH",
                path="/developer/v1/agents/{agent_id}",
                path_params=_without_not_given({"agent_id": agent_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "description": description,
                        "name": name,
                        "owner_id": owner_id,
                        "role_ids": role_ids,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_AGENTS_UPDATE_METADATA,
            ),
        )


class Applications:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def delete_document(
        self,
        *,
        document_id: str,
        data_source_summary: str,
        user_prompt: str,
    ) -> EmptyObject:
        """Delete a document from the current financing application (delete_application_document_detail_resource)."""
        return cast(
            EmptyObject,
            self._transport.request(
                method="DELETE",
                path="/developer/v1/applications/documents/{document_id}",
                path_params=_without_not_given({"document_id": document_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_DELETE_DOCUMENT_METADATA,
            ),
        )

    def documents(
        self,
        *,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiApplicationDocumentResource:
        """List documents uploaded for the current financing application (get_application_document_resource)."""
        return cast(
            PaginatedResponseApiApplicationDocumentResource,
            self._transport.request(
                method="GET",
                path="/developer/v1/applications/documents",
                path_params=None,
                params=_without_not_given({"start": start, "page_size": page_size}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_DOCUMENTS_METADATA,
            ),
        )

    def edit(
        self,
        *,
        data_source_summary: str,
        user_prompt: str,
        beneficial_owners: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        business: dict[str, Any] | NotGiven = NOT_GIVEN,
        controlling_officer: dict[str, Any] | NotGiven = NOT_GIVEN,
        financial_details: dict[str, Any] | NotGiven = NOT_GIVEN,
        manual_bank_account: dict[str, Any] | NotGiven = NOT_GIVEN,
        open_ramp_checking_account: bool | NotGiven = NOT_GIVEN,
        ownership_acknowledgement: str | NotGiven = NOT_GIVEN,
    ) -> ApiApplicationResource:
        """Update a financing application (patch_application_update_resource)."""
        return cast(
            ApiApplicationResource,
            self._transport.request(
                method="PATCH",
                path="/developer/v1/applications",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "beneficial_owners": beneficial_owners,
                        "business": business,
                        "controlling_officer": controlling_officer,
                        "financial_details": financial_details,
                        "manual_bank_account": manual_bank_account,
                        "open_ramp_checking_account": open_ramp_checking_account,
                        "ownership_acknowledgement": ownership_acknowledgement,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_EDIT_METADATA,
            ),
        )

    def followups(
        self,
    ) -> ApiFollowupListResource:
        """Fetch customer-pending financing application follow-ups (get_application_followup_list_resource)."""
        return cast(
            ApiFollowupListResource,
            self._transport.request(
                method="GET",
                path="/developer/v1/applications/followups",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_FOLLOWUPS_METADATA,
            ),
        )

    def get(
        self,
    ) -> ApiApplicationResource:
        """Fetch a financing application (get_application_resource)."""
        return cast(
            ApiApplicationResource,
            self._transport.request(
                method="GET",
                path="/developer/v1/applications",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_GET_METADATA,
            ),
        )

    def progress(
        self,
    ) -> ApiApplicationProgressResource:
        """Fetch financing application progress (get_application_progress_resource)."""
        return cast(
            ApiApplicationProgressResource,
            self._transport.request(
                method="GET",
                path="/developer/v1/applications/progress",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_PROGRESS_METADATA,
            ),
        )

    def submit(
        self,
        *,
        data_source_summary: str,
        user_prompt: str,
    ) -> None:
        """Submit completed customer-pending financing application follow-ups (post_application_followup_submit_resource)."""
        self._transport.request(
            method="POST",
            path="/developer/v1/applications/followups/submit",
            path_params=None,
            params=None,
            headers=None,
            json=_without_not_given(
                {"data_source_summary": data_source_summary, "user_prompt": user_prompt}
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_APPLICATIONS_SUBMIT_METADATA,
        )
        return None

    def update_followup(
        self,
        *,
        followup_id: str,
        data_source_summary: str,
        user_prompt: str,
        no_more_accounts_to_link: bool | NotGiven = NOT_GIVEN,
        response_text: str | NotGiven = NOT_GIVEN,
        selected_document_type: str | NotGiven = NOT_GIVEN,
    ) -> ApiFollowupResource:
        """Update an agent-editable financing application follow-up (patch_application_followup_resource)."""
        return cast(
            ApiFollowupResource,
            self._transport.request(
                method="PATCH",
                path="/developer/v1/applications/followups/{followup_id}",
                path_params=_without_not_given({"followup_id": followup_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "no_more_accounts_to_link": no_more_accounts_to_link,
                        "response_text": response_text,
                        "selected_document_type": selected_document_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_UPDATE_FOLLOWUP_METADATA,
            ),
        )

    def upload(
        self,
        *,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        data_source_summary: str,
        user_prompt: str,
        file: FileInput,
        followup_id: UUID | None | NotGiven = NOT_GIVEN,
        manual_bank_account_id: UUID | None | NotGiven = NOT_GIVEN,
        purpose: str,
    ) -> ApiApplicationDocumentResource:
        """Upload a document for the current financing application (post_application_document_resource)."""
        return cast(
            ApiApplicationDocumentResource,
            self._transport.request(
                method="POST",
                path="/developer/v1/applications/documents",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=None,
                data=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "followup_id": followup_id,
                        "manual_bank_account_id": manual_bank_account_id,
                        "purpose": purpose,
                    }
                ),
                files=_without_not_given({"file": file}),
                metadata=_DEVELOPER_API_APPLICATIONS_UPLOAD_METADATA,
            ),
        )


class AsyncApplications:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def delete_document(
        self,
        *,
        document_id: str,
        data_source_summary: str,
        user_prompt: str,
    ) -> EmptyObject:
        """Delete a document from the current financing application (delete_application_document_detail_resource)."""
        return cast(
            EmptyObject,
            await self._transport.request(
                method="DELETE",
                path="/developer/v1/applications/documents/{document_id}",
                path_params=_without_not_given({"document_id": document_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_DELETE_DOCUMENT_METADATA,
            ),
        )

    async def documents(
        self,
        *,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiApplicationDocumentResource:
        """List documents uploaded for the current financing application (get_application_document_resource)."""
        return cast(
            PaginatedResponseApiApplicationDocumentResource,
            await self._transport.request(
                method="GET",
                path="/developer/v1/applications/documents",
                path_params=None,
                params=_without_not_given({"start": start, "page_size": page_size}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_DOCUMENTS_METADATA,
            ),
        )

    async def edit(
        self,
        *,
        data_source_summary: str,
        user_prompt: str,
        beneficial_owners: Sequence[dict[str, Any]] | NotGiven = NOT_GIVEN,
        business: dict[str, Any] | NotGiven = NOT_GIVEN,
        controlling_officer: dict[str, Any] | NotGiven = NOT_GIVEN,
        financial_details: dict[str, Any] | NotGiven = NOT_GIVEN,
        manual_bank_account: dict[str, Any] | NotGiven = NOT_GIVEN,
        open_ramp_checking_account: bool | NotGiven = NOT_GIVEN,
        ownership_acknowledgement: str | NotGiven = NOT_GIVEN,
    ) -> ApiApplicationResource:
        """Update a financing application (patch_application_update_resource)."""
        return cast(
            ApiApplicationResource,
            await self._transport.request(
                method="PATCH",
                path="/developer/v1/applications",
                path_params=None,
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "beneficial_owners": beneficial_owners,
                        "business": business,
                        "controlling_officer": controlling_officer,
                        "financial_details": financial_details,
                        "manual_bank_account": manual_bank_account,
                        "open_ramp_checking_account": open_ramp_checking_account,
                        "ownership_acknowledgement": ownership_acknowledgement,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_EDIT_METADATA,
            ),
        )

    async def followups(
        self,
    ) -> ApiFollowupListResource:
        """Fetch customer-pending financing application follow-ups (get_application_followup_list_resource)."""
        return cast(
            ApiFollowupListResource,
            await self._transport.request(
                method="GET",
                path="/developer/v1/applications/followups",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_FOLLOWUPS_METADATA,
            ),
        )

    async def get(
        self,
    ) -> ApiApplicationResource:
        """Fetch a financing application (get_application_resource)."""
        return cast(
            ApiApplicationResource,
            await self._transport.request(
                method="GET",
                path="/developer/v1/applications",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_GET_METADATA,
            ),
        )

    async def progress(
        self,
    ) -> ApiApplicationProgressResource:
        """Fetch financing application progress (get_application_progress_resource)."""
        return cast(
            ApiApplicationProgressResource,
            await self._transport.request(
                method="GET",
                path="/developer/v1/applications/progress",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_PROGRESS_METADATA,
            ),
        )

    async def submit(
        self,
        *,
        data_source_summary: str,
        user_prompt: str,
    ) -> None:
        """Submit completed customer-pending financing application follow-ups (post_application_followup_submit_resource)."""
        await self._transport.request(
            method="POST",
            path="/developer/v1/applications/followups/submit",
            path_params=None,
            params=None,
            headers=None,
            json=_without_not_given(
                {"data_source_summary": data_source_summary, "user_prompt": user_prompt}
            ),
            data=None,
            files=None,
            metadata=_DEVELOPER_API_APPLICATIONS_SUBMIT_METADATA,
        )
        return None

    async def update_followup(
        self,
        *,
        followup_id: str,
        data_source_summary: str,
        user_prompt: str,
        no_more_accounts_to_link: bool | NotGiven = NOT_GIVEN,
        response_text: str | NotGiven = NOT_GIVEN,
        selected_document_type: str | NotGiven = NOT_GIVEN,
    ) -> ApiFollowupResource:
        """Update an agent-editable financing application follow-up (patch_application_followup_resource)."""
        return cast(
            ApiFollowupResource,
            await self._transport.request(
                method="PATCH",
                path="/developer/v1/applications/followups/{followup_id}",
                path_params=_without_not_given({"followup_id": followup_id}),
                params=None,
                headers=None,
                json=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "no_more_accounts_to_link": no_more_accounts_to_link,
                        "response_text": response_text,
                        "selected_document_type": selected_document_type,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_APPLICATIONS_UPDATE_FOLLOWUP_METADATA,
            ),
        )

    async def upload(
        self,
        *,
        idempotency_key: str | NotGiven = NOT_GIVEN,
        data_source_summary: str,
        user_prompt: str,
        file: FileInput,
        followup_id: UUID | None | NotGiven = NOT_GIVEN,
        manual_bank_account_id: UUID | None | NotGiven = NOT_GIVEN,
        purpose: str,
    ) -> ApiApplicationDocumentResource:
        """Upload a document for the current financing application (post_application_document_resource)."""
        return cast(
            ApiApplicationDocumentResource,
            await self._transport.request(
                method="POST",
                path="/developer/v1/applications/documents",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=None,
                data=_without_not_given(
                    {
                        "data_source_summary": data_source_summary,
                        "user_prompt": user_prompt,
                        "followup_id": followup_id,
                        "manual_bank_account_id": manual_bank_account_id,
                        "purpose": purpose,
                    }
                ),
                files=_without_not_given({"file": file}),
                metadata=_DEVELOPER_API_APPLICATIONS_UPLOAD_METADATA,
            ),
        )


class AskRamp:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def ask(
        self,
        *,
        idempotency_key: str,
        question: str,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Start a durable AskRamp session for Ramp questions (post_ask_ramp_sessions_resource)."""
        return cast(
            AskRampExternalResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/ask-ramp/sessions",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {"question": question, "wait_seconds": wait_seconds}
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_ASK_METADATA,
            ),
        )

    def continue_(
        self,
        *,
        session_id: UUID,
        idempotency_key: str,
        input_request_id: str | None | NotGiven = NOT_GIVEN,
        response: str,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Continue a stable AskRamp session (post_ask_ramp_session_messages_resource)."""
        return cast(
            AskRampExternalResult,
            self._transport.request(
                method="POST",
                path="/developer/v1/ask-ramp/sessions/{session_id}/messages",
                path_params=_without_not_given({"session_id": session_id}),
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "input_request_id": input_request_id,
                        "response": response,
                        "wait_seconds": wait_seconds,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_CONTINUE__METADATA,
            ),
        )

    def get_result(
        self,
        *,
        session_id: UUID,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Get the current result for a read-only AskRamp session (get_ask_ramp_session_result_resource)."""
        return cast(
            AskRampExternalResult,
            self._transport.request(
                method="GET",
                path="/developer/v1/ask-ramp/sessions/{session_id}",
                path_params=_without_not_given({"session_id": session_id}),
                params=_without_not_given({"wait_seconds": wait_seconds}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_GET_RESULT_METADATA,
            ),
        )


class AsyncAskRamp:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def ask(
        self,
        *,
        idempotency_key: str,
        question: str,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Start a durable AskRamp session for Ramp questions (post_ask_ramp_sessions_resource)."""
        return cast(
            AskRampExternalResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/ask-ramp/sessions",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {"question": question, "wait_seconds": wait_seconds}
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_ASK_METADATA,
            ),
        )

    async def continue_(
        self,
        *,
        session_id: UUID,
        idempotency_key: str,
        input_request_id: str | None | NotGiven = NOT_GIVEN,
        response: str,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Continue a stable AskRamp session (post_ask_ramp_session_messages_resource)."""
        return cast(
            AskRampExternalResult,
            await self._transport.request(
                method="POST",
                path="/developer/v1/ask-ramp/sessions/{session_id}/messages",
                path_params=_without_not_given({"session_id": session_id}),
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "input_request_id": input_request_id,
                        "response": response,
                        "wait_seconds": wait_seconds,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_CONTINUE__METADATA,
            ),
        )

    async def get_result(
        self,
        *,
        session_id: UUID,
        wait_seconds: int | NotGiven = NOT_GIVEN,
    ) -> AskRampExternalResult:
        """Get the current result for a read-only AskRamp session (get_ask_ramp_session_result_resource)."""
        return cast(
            AskRampExternalResult,
            await self._transport.request(
                method="GET",
                path="/developer/v1/ask-ramp/sessions/{session_id}",
                path_params=_without_not_given({"session_id": session_id}),
                params=_without_not_given({"wait_seconds": wait_seconds}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_ASK_RAMP_GET_RESULT_METADATA,
            ),
        )


class BankLink:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def accounts(
        self,
        *,
        connection_provider: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiBankAccountResource:
        """List bank accounts (get_bank_account_list_with_pagination)."""
        return cast(
            PaginatedResponseApiBankAccountResource,
            self._transport.request(
                method="GET",
                path="/developer/v1/bank-accounts",
                path_params=None,
                params=_without_not_given(
                    {
                        "connection_provider": connection_provider,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_BANK_LINK_ACCOUNTS_METADATA,
            ),
        )

    def create(
        self,
        *,
        idempotency_key: str,
        account_name: str | None | NotGiven = NOT_GIVEN,
        account_number: str,
        account_subtype: str,
        routing_number: str,
        wire_details: dict[str, Any] | None | NotGiven = NOT_GIVEN,
    ) -> ApiBankAccountResource:
        """Create a manually connected bank account (post_bank_account_create)."""
        return cast(
            ApiBankAccountResource,
            self._transport.request(
                method="POST",
                path="/developer/v1/bank-accounts",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "account_name": account_name,
                        "account_number": account_number,
                        "account_subtype": account_subtype,
                        "routing_number": routing_number,
                        "wire_details": wire_details,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_BANK_LINK_CREATE_METADATA,
            ),
        )


class AsyncBankLink:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def accounts(
        self,
        *,
        connection_provider: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiBankAccountResource:
        """List bank accounts (get_bank_account_list_with_pagination)."""
        return cast(
            PaginatedResponseApiBankAccountResource,
            await self._transport.request(
                method="GET",
                path="/developer/v1/bank-accounts",
                path_params=None,
                params=_without_not_given(
                    {
                        "connection_provider": connection_provider,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_BANK_LINK_ACCOUNTS_METADATA,
            ),
        )

    async def create(
        self,
        *,
        idempotency_key: str,
        account_name: str | None | NotGiven = NOT_GIVEN,
        account_number: str,
        account_subtype: str,
        routing_number: str,
        wire_details: dict[str, Any] | None | NotGiven = NOT_GIVEN,
    ) -> ApiBankAccountResource:
        """Create a manually connected bank account (post_bank_account_create)."""
        return cast(
            ApiBankAccountResource,
            await self._transport.request(
                method="POST",
                path="/developer/v1/bank-accounts",
                path_params=None,
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "account_name": account_name,
                        "account_number": account_number,
                        "account_subtype": account_subtype,
                        "routing_number": routing_number,
                        "wire_details": wire_details,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_BANK_LINK_CREATE_METADATA,
            ),
        )


class Merchant:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def list(
        self,
        *,
        merchant_url: str | NotGiven = NOT_GIVEN,
        merchant_name: str | NotGiven = NOT_GIVEN,
        transaction_from_date: str | NotGiven = NOT_GIVEN,
        transaction_to_date: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiMerchantResourceSchema:
        """List merchants (get_merchant_list_with_pagination)."""
        return cast(
            PaginatedResponseApiMerchantResourceSchema,
            self._transport.request(
                method="GET",
                path="/developer/v1/merchants",
                path_params=None,
                params=_without_not_given(
                    {
                        "merchant_url": merchant_url,
                        "merchant_name": merchant_name,
                        "transaction_from_date": transaction_from_date,
                        "transaction_to_date": transaction_to_date,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_MERCHANT_LIST_METADATA,
            ),
        )


class AsyncMerchant:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def list(
        self,
        *,
        merchant_url: str | NotGiven = NOT_GIVEN,
        merchant_name: str | NotGiven = NOT_GIVEN,
        transaction_from_date: str | NotGiven = NOT_GIVEN,
        transaction_to_date: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiMerchantResourceSchema:
        """List merchants (get_merchant_list_with_pagination)."""
        return cast(
            PaginatedResponseApiMerchantResourceSchema,
            await self._transport.request(
                method="GET",
                path="/developer/v1/merchants",
                path_params=None,
                params=_without_not_given(
                    {
                        "merchant_url": merchant_url,
                        "merchant_name": merchant_name,
                        "transaction_from_date": transaction_from_date,
                        "transaction_to_date": transaction_to_date,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_MERCHANT_LIST_METADATA,
            ),
        )


class Sourcing:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def upload(
        self,
        *,
        file: FileInput,
    ) -> ApiSourcingUploadDocumentResultJsonMode:
        """Upload a document for use as an RFX cover-sheet or pricing-sheet attachment (post_agent_tool_api___upload_sourcing_document)."""
        return cast(
            ApiSourcingUploadDocumentResultJsonMode,
            self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/upload-sourcing-document",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=_without_not_given({"file": file}),
                metadata=_DEVELOPER_API_SOURCING_UPLOAD_METADATA,
            ),
        )


class AsyncSourcing:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def upload(
        self,
        *,
        file: FileInput,
    ) -> ApiSourcingUploadDocumentResultJsonMode:
        """Upload a document for use as an RFX cover-sheet or pricing-sheet attachment (post_agent_tool_api___upload_sourcing_document)."""
        return cast(
            ApiSourcingUploadDocumentResultJsonMode,
            await self._transport.request(
                method="POST",
                path="/developer/v1/agent-tools/upload-sourcing-document",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=_without_not_given({"file": file}),
                metadata=_DEVELOPER_API_SOURCING_UPLOAD_METADATA,
            ),
        )


class Statements:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def get(
        self,
        *,
        statement_id: str,
    ) -> Statement:
        """Fetch a statement (get_statement_resource)."""
        return cast(
            Statement,
            self._transport.request(
                method="GET",
                path="/developer/v1/statements/{statement_id}",
                path_params=_without_not_given({"statement_id": statement_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_STATEMENTS_GET_METADATA,
            ),
        )

    def list(
        self,
        *,
        from_date: str | NotGiven = NOT_GIVEN,
        to_date: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiStatementResourceSchema:
        """List statements (get_statement_list_with_pagination)."""
        return cast(
            PaginatedResponseApiStatementResourceSchema,
            self._transport.request(
                method="GET",
                path="/developer/v1/statements",
                path_params=None,
                params=_without_not_given(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_STATEMENTS_LIST_METADATA,
            ),
        )


class AsyncStatements:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def get(
        self,
        *,
        statement_id: str,
    ) -> Statement:
        """Fetch a statement (get_statement_resource)."""
        return cast(
            Statement,
            await self._transport.request(
                method="GET",
                path="/developer/v1/statements/{statement_id}",
                path_params=_without_not_given({"statement_id": statement_id}),
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_STATEMENTS_GET_METADATA,
            ),
        )

    async def list(
        self,
        *,
        from_date: str | NotGiven = NOT_GIVEN,
        to_date: str | NotGiven = NOT_GIVEN,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseApiStatementResourceSchema:
        """List statements (get_statement_list_with_pagination)."""
        return cast(
            PaginatedResponseApiStatementResourceSchema,
            await self._transport.request(
                method="GET",
                path="/developer/v1/statements",
                path_params=None,
                params=_without_not_given(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                        "start": start,
                        "page_size": page_size,
                    }
                ),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_STATEMENTS_LIST_METADATA,
            ),
        )


class Transactions:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def split(
        self,
        *,
        transaction_id: str,
        line_items: Sequence[dict[str, Any]] | None,
    ) -> SingleTransaction:
        """Split a transaction into line items, or update an existing split (patch_transaction_canonical_update_resource)."""
        return cast(
            SingleTransaction,
            self._transport.request(
                method="PATCH",
                path="/developer/v1/transactions/{transaction_id}",
                path_params=_without_not_given({"transaction_id": transaction_id}),
                params=None,
                headers=None,
                json=_without_not_given({"line_items": line_items}),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TRANSACTIONS_SPLIT_METADATA,
            ),
        )


class AsyncTransactions:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def split(
        self,
        *,
        transaction_id: str,
        line_items: Sequence[dict[str, Any]] | None,
    ) -> SingleTransaction:
        """Split a transaction into line items, or update an existing split (patch_transaction_canonical_update_resource)."""
        return cast(
            SingleTransaction,
            await self._transport.request(
                method="PATCH",
                path="/developer/v1/transactions/{transaction_id}",
                path_params=_without_not_given({"transaction_id": transaction_id}),
                params=None,
                headers=None,
                json=_without_not_given({"line_items": line_items}),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TRANSACTIONS_SPLIT_METADATA,
            ),
        )


class Treasury:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def account_numbers(
        self,
        *,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseAgentAccountNumberResponse:
        """List agent account numbers (get_agent_account_numbers_list_resource)."""
        return cast(
            PaginatedResponseAgentAccountNumberResponse,
            self._transport.request(
                method="GET",
                path="/developer/v1/banking/agent-account-numbers",
                path_params=None,
                params=_without_not_given({"start": start, "page_size": page_size}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TREASURY_ACCOUNT_NUMBERS_METADATA,
            ),
        )

    def request_funds(
        self,
        *,
        banking_account_id: str,
        idempotency_key: str,
        agent_account_number_id: UUID | None | NotGiven = NOT_GIVEN,
        amount: dict[str, Any],
        external_bank_account_id: UUID,
        memo: str | None | NotGiven = NOT_GIVEN,
    ) -> DrawdownRequestResponse:
        """Request funds for a banking account (post_banking_drawdown_requests_resource)."""
        return cast(
            DrawdownRequestResponse,
            self._transport.request(
                method="POST",
                path="/developer/v1/banking/accounts/{banking_account_id}/drawdown-requests",
                path_params=_without_not_given(
                    {"banking_account_id": banking_account_id}
                ),
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "agent_account_number_id": agent_account_number_id,
                        "amount": amount,
                        "external_bank_account_id": external_bank_account_id,
                        "memo": memo,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TREASURY_REQUEST_FUNDS_METADATA,
            ),
        )


class AsyncTreasury:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def account_numbers(
        self,
        *,
        start: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
    ) -> PaginatedResponseAgentAccountNumberResponse:
        """List agent account numbers (get_agent_account_numbers_list_resource)."""
        return cast(
            PaginatedResponseAgentAccountNumberResponse,
            await self._transport.request(
                method="GET",
                path="/developer/v1/banking/agent-account-numbers",
                path_params=None,
                params=_without_not_given({"start": start, "page_size": page_size}),
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TREASURY_ACCOUNT_NUMBERS_METADATA,
            ),
        )

    async def request_funds(
        self,
        *,
        banking_account_id: str,
        idempotency_key: str,
        agent_account_number_id: UUID | None | NotGiven = NOT_GIVEN,
        amount: dict[str, Any],
        external_bank_account_id: UUID,
        memo: str | None | NotGiven = NOT_GIVEN,
    ) -> DrawdownRequestResponse:
        """Request funds for a banking account (post_banking_drawdown_requests_resource)."""
        return cast(
            DrawdownRequestResponse,
            await self._transport.request(
                method="POST",
                path="/developer/v1/banking/accounts/{banking_account_id}/drawdown-requests",
                path_params=_without_not_given(
                    {"banking_account_id": banking_account_id}
                ),
                params=None,
                headers=_without_not_given({"X-Idempotency-Key": idempotency_key}),
                json=_without_not_given(
                    {
                        "agent_account_number_id": agent_account_number_id,
                        "amount": amount,
                        "external_bank_account_id": external_bank_account_id,
                        "memo": memo,
                    }
                ),
                data=None,
                files=None,
                metadata=_DEVELOPER_API_TREASURY_REQUEST_FUNDS_METADATA,
            ),
        )


class Users:
    def __init__(self, transport: SyncTransport) -> None:
        self._transport = transport

    def roles(
        self,
    ) -> ApiRolesList:
        """List custom roles (get_roles_resource)."""
        return cast(
            ApiRolesList,
            self._transport.request(
                method="GET",
                path="/developer/v1/roles",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_USERS_ROLES_METADATA,
            ),
        )


class AsyncUsers:
    def __init__(self, transport: AsyncTransport) -> None:
        self._transport = transport

    async def roles(
        self,
    ) -> ApiRolesList:
        """List custom roles (get_roles_resource)."""
        return cast(
            ApiRolesList,
            await self._transport.request(
                method="GET",
                path="/developer/v1/roles",
                path_params=None,
                params=None,
                headers=None,
                json=None,
                data=None,
                files=None,
                metadata=_DEVELOPER_API_USERS_ROLES_METADATA,
            ),
        )


class AgentTools:
    def __init__(self, transport: SyncTransport) -> None:
        self.accounting = AgentToolsAccounting(transport)
        self.agent_cards = AgentToolsAgentCards(transport)
        self.ai_token_spend = AgentToolsAiTokenSpend(transport)
        self.analyst = AgentToolsAnalyst(transport)
        self.bills = AgentToolsBills(transport)
        self.business = AgentToolsBusiness(transport)
        self.cards = AgentToolsCards(transport)
        self.communication = AgentToolsCommunication(transport)
        self.declines = AgentToolsDeclines(transport)
        self.external_agents = AgentToolsExternalAgents(transport)
        self.funds = AgentToolsFunds(transport)
        self.general = AgentToolsGeneral(transport)
        self.merchant = AgentToolsMerchant(transport)
        self.policy = AgentToolsPolicy(transport)
        self.procurement_requests = AgentToolsProcurementRequests(transport)
        self.purchase_orders = AgentToolsPurchaseOrders(transport)
        self.receipts = AgentToolsReceipts(transport)
        self.reimbursements = AgentToolsReimbursements(transport)
        self.requests = AgentToolsRequests(transport)
        self.research = AgentToolsResearch(transport)
        self.sourcing = AgentToolsSourcing(transport)
        self.statements = AgentToolsStatements(transport)
        self.tasks = AgentToolsTasks(transport)
        self.transactions = AgentToolsTransactions(transport)
        self.travel = AgentToolsTravel(transport)
        self.treasury = AgentToolsTreasury(transport)
        self.users = AgentToolsUsers(transport)
        self.vendors = AgentToolsVendors(transport)
        self.x402 = AgentToolsX402(transport)


class AsyncAgentTools:
    def __init__(self, transport: AsyncTransport) -> None:
        self.accounting = AsyncAgentToolsAccounting(transport)
        self.agent_cards = AsyncAgentToolsAgentCards(transport)
        self.ai_token_spend = AsyncAgentToolsAiTokenSpend(transport)
        self.analyst = AsyncAgentToolsAnalyst(transport)
        self.bills = AsyncAgentToolsBills(transport)
        self.business = AsyncAgentToolsBusiness(transport)
        self.cards = AsyncAgentToolsCards(transport)
        self.communication = AsyncAgentToolsCommunication(transport)
        self.declines = AsyncAgentToolsDeclines(transport)
        self.external_agents = AsyncAgentToolsExternalAgents(transport)
        self.funds = AsyncAgentToolsFunds(transport)
        self.general = AsyncAgentToolsGeneral(transport)
        self.merchant = AsyncAgentToolsMerchant(transport)
        self.policy = AsyncAgentToolsPolicy(transport)
        self.procurement_requests = AsyncAgentToolsProcurementRequests(transport)
        self.purchase_orders = AsyncAgentToolsPurchaseOrders(transport)
        self.receipts = AsyncAgentToolsReceipts(transport)
        self.reimbursements = AsyncAgentToolsReimbursements(transport)
        self.requests = AsyncAgentToolsRequests(transport)
        self.research = AsyncAgentToolsResearch(transport)
        self.sourcing = AsyncAgentToolsSourcing(transport)
        self.statements = AsyncAgentToolsStatements(transport)
        self.tasks = AsyncAgentToolsTasks(transport)
        self.transactions = AsyncAgentToolsTransactions(transport)
        self.travel = AsyncAgentToolsTravel(transport)
        self.treasury = AsyncAgentToolsTreasury(transport)
        self.users = AsyncAgentToolsUsers(transport)
        self.vendors = AsyncAgentToolsVendors(transport)
        self.x402 = AsyncAgentToolsX402(transport)


class Ramp:
    def __init__(self, *, transport: SyncTransport) -> None:
        self.accounting = Accounting(transport)
        self.agent_wallet = AgentWallet(transport)
        self.agents = Agents(transport)
        self.applications = Applications(transport)
        self.ask_ramp = AskRamp(transport)
        self.bank_link = BankLink(transport)
        self.merchant = Merchant(transport)
        self.sourcing = Sourcing(transport)
        self.statements = Statements(transport)
        self.transactions = Transactions(transport)
        self.treasury = Treasury(transport)
        self.users = Users(transport)
        self.agent_tools = AgentTools(transport)


class AsyncRamp:
    def __init__(self, *, transport: AsyncTransport) -> None:
        self.accounting = AsyncAccounting(transport)
        self.agent_wallet = AsyncAgentWallet(transport)
        self.agents = AsyncAgents(transport)
        self.applications = AsyncApplications(transport)
        self.ask_ramp = AsyncAskRamp(transport)
        self.bank_link = AsyncBankLink(transport)
        self.merchant = AsyncMerchant(transport)
        self.sourcing = AsyncSourcing(transport)
        self.statements = AsyncStatements(transport)
        self.transactions = AsyncTransactions(transport)
        self.treasury = AsyncTreasury(transport)
        self.users = AsyncUsers(transport)
        self.agent_tools = AsyncAgentTools(transport)
