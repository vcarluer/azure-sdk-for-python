# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import AbnormalTimePeriod
    from ._models_py3 import Address
    from ._models_py3 import AddressResponse
    from ._models_py3 import AnalysisData
    from ._models_py3 import AnalysisDefinition
    from ._models_py3 import ApiDefinitionInfo
    from ._models_py3 import ApiKVReference
    from ._models_py3 import ApiManagementConfig
    from ._models_py3 import ApplicationLogsConfig
    from ._models_py3 import ApplicationStack
    from ._models_py3 import ApplicationStackResource
    from ._models_py3 import AppServiceCertificate
    from ._models_py3 import AppServiceCertificateOrder
    from ._models_py3 import AppServiceCertificateOrderPatchResource
    from ._models_py3 import AppServiceCertificatePatchResource
    from ._models_py3 import AppServiceCertificateResource
    from ._models_py3 import AppServiceEnvironment
    from ._models_py3 import AppServiceEnvironmentPatchResource
    from ._models_py3 import AppServiceEnvironmentResource
    from ._models_py3 import AppServicePlan
    from ._models_py3 import AppServicePlanPatchResource
    from ._models_py3 import ArmIdWrapper
    from ._models_py3 import AutoHealActions
    from ._models_py3 import AutoHealCustomAction
    from ._models_py3 import AutoHealRules
    from ._models_py3 import AutoHealTriggers
    from ._models_py3 import AzureBlobStorageApplicationLogsConfig
    from ._models_py3 import AzureBlobStorageHttpLogsConfig
    from ._models_py3 import AzureStorageInfoValue
    from ._models_py3 import AzureStoragePropertyDictionaryResource
    from ._models_py3 import AzureTableStorageApplicationLogsConfig
    from ._models_py3 import BackupItem
    from ._models_py3 import BackupRequest
    from ._models_py3 import BackupSchedule
    from ._models_py3 import BillingMeter
    from ._models_py3 import Capability
    from ._models_py3 import Certificate
    from ._models_py3 import CertificateDetails
    from ._models_py3 import CertificateEmail
    from ._models_py3 import CertificateOrderAction
    from ._models_py3 import CertificatePatchResource
    from ._models_py3 import CloningInfo
    from ._models_py3 import ConnectionStringDictionary
    from ._models_py3 import ConnStringInfo
    from ._models_py3 import ConnStringValueTypePair
    from ._models_py3 import Contact
    from ._models_py3 import ContainerCpuStatistics
    from ._models_py3 import ContainerCpuUsage
    from ._models_py3 import ContainerInfo
    from ._models_py3 import ContainerMemoryStatistics
    from ._models_py3 import ContainerNetworkInterfaceStatistics
    from ._models_py3 import ContainerThrottlingData
    from ._models_py3 import ContinuousWebJob
    from ._models_py3 import CorsSettings
    from ._models_py3 import CsmCopySlotEntity
    from ._models_py3 import CsmMoveResourceEnvelope
    from ._models_py3 import CsmOperationDescription
    from ._models_py3 import CsmOperationDescriptionProperties
    from ._models_py3 import CsmOperationDisplay
    from ._models_py3 import CsmPublishingProfileOptions
    from ._models_py3 import CsmSlotEntity
    from ._models_py3 import CsmUsageQuota
    from ._models_py3 import CustomHostnameAnalysisResult
    from ._models_py3 import DatabaseBackupSetting
    from ._models_py3 import DataSource
    from ._models_py3 import DataTableResponseColumn
    from ._models_py3 import DataTableResponseObject
    from ._models_py3 import DefaultErrorResponse, DefaultErrorResponseException
    from ._models_py3 import DefaultErrorResponseError
    from ._models_py3 import DefaultErrorResponseErrorDetailsItem
    from ._models_py3 import DeletedAppRestoreRequest
    from ._models_py3 import DeletedSite
    from ._models_py3 import Deployment
    from ._models_py3 import DeploymentLocations
    from ._models_py3 import DetectorAbnormalTimePeriod
    from ._models_py3 import DetectorDefinition
    from ._models_py3 import DetectorInfo
    from ._models_py3 import DetectorResponse
    from ._models_py3 import DiagnosticAnalysis
    from ._models_py3 import DiagnosticCategory
    from ._models_py3 import DiagnosticData
    from ._models_py3 import DiagnosticDetectorResponse
    from ._models_py3 import DiagnosticMetricSample
    from ._models_py3 import DiagnosticMetricSet
    from ._models_py3 import Dimension
    from ._models_py3 import Domain
    from ._models_py3 import DomainAvailabilityCheckResult
    from ._models_py3 import DomainControlCenterSsoRequest
    from ._models_py3 import DomainOwnershipIdentifier
    from ._models_py3 import DomainPatchResource
    from ._models_py3 import DomainPurchaseConsent
    from ._models_py3 import DomainRecommendationSearchParameters
    from ._models_py3 import EnabledConfig
    from ._models_py3 import EndpointDependency
    from ._models_py3 import EndpointDetail
    from ._models_py3 import ErrorEntity
    from ._models_py3 import Experiments
    from ._models_py3 import FileSystemApplicationLogsConfig
    from ._models_py3 import FileSystemHttpLogsConfig
    from ._models_py3 import FunctionEnvelope
    from ._models_py3 import FunctionSecrets
    from ._models_py3 import GeoRegion
    from ._models_py3 import GlobalCsmSkuDescription
    from ._models_py3 import HandlerMapping
    from ._models_py3 import HostingEnvironmentDeploymentInfo
    from ._models_py3 import HostingEnvironmentDiagnostics
    from ._models_py3 import HostingEnvironmentProfile
    from ._models_py3 import HostKeys
    from ._models_py3 import HostName
    from ._models_py3 import HostNameBinding
    from ._models_py3 import HostNameSslState
    from ._models_py3 import HttpLogsConfig
    from ._models_py3 import HybridConnection
    from ._models_py3 import HybridConnectionKey
    from ._models_py3 import HybridConnectionLimits
    from ._models_py3 import Identifier
    from ._models_py3 import InboundEnvironmentEndpoint
    from ._models_py3 import IpSecurityRestriction
    from ._models_py3 import KeyInfo
    from ._models_py3 import KeyVaultReferenceCollection
    from ._models_py3 import KeyVaultReferenceResource
    from ._models_py3 import LocalizableString
    from ._models_py3 import LogSpecification
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import ManagedServiceIdentityUserAssignedIdentitiesValue
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricSpecification
    from ._models_py3 import MigrateMySqlRequest
    from ._models_py3 import MigrateMySqlStatus
    from ._models_py3 import MSDeploy
    from ._models_py3 import MSDeployLog
    from ._models_py3 import MSDeployLogEntry
    from ._models_py3 import MSDeployStatus
    from ._models_py3 import NameIdentifier
    from ._models_py3 import NameValuePair
    from ._models_py3 import NetworkAccessControlEntry
    from ._models_py3 import NetworkFeatures
    from ._models_py3 import NetworkTrace
    from ._models_py3 import Operation
    from ._models_py3 import OutboundEnvironmentEndpoint
    from ._models_py3 import PerfMonResponse
    from ._models_py3 import PerfMonSample
    from ._models_py3 import PerfMonSet
    from ._models_py3 import PremierAddOn
    from ._models_py3 import PremierAddOnOffer
    from ._models_py3 import PremierAddOnPatchResource
    from ._models_py3 import PrivateAccess
    from ._models_py3 import PrivateAccessSubnet
    from ._models_py3 import PrivateAccessVirtualNetwork
    from ._models_py3 import PrivateEndpointConnectionResource
    from ._models_py3 import PrivateLinkConnectionApprovalRequestResource
    from ._models_py3 import PrivateLinkConnectionState
    from ._models_py3 import PrivateLinkResource
    from ._models_py3 import PrivateLinkResourceProperties
    from ._models_py3 import PrivateLinkResourcesWrapper
    from ._models_py3 import ProcessInfo
    from ._models_py3 import ProcessModuleInfo
    from ._models_py3 import ProcessThreadInfo
    from ._models_py3 import ProxyOnlyResource
    from ._models_py3 import PublicCertificate
    from ._models_py3 import PushSettings
    from ._models_py3 import RampUpRule
    from ._models_py3 import Recommendation
    from ._models_py3 import RecommendationRule
    from ._models_py3 import ReissueCertificateOrderRequest
    from ._models_py3 import RelayServiceConnectionEntity
    from ._models_py3 import Rendering
    from ._models_py3 import RenewCertificateOrderRequest
    from ._models_py3 import RequestsBasedTrigger
    from ._models_py3 import Resource
    from ._models_py3 import ResourceHealthMetadata
    from ._models_py3 import ResourceMetricAvailability
    from ._models_py3 import ResourceMetricDefinition
    from ._models_py3 import ResourceNameAvailability
    from ._models_py3 import ResourceNameAvailabilityRequest
    from ._models_py3 import ResponseMetaData
    from ._models_py3 import RestoreRequest
    from ._models_py3 import ServiceSpecification
    from ._models_py3 import Site
    from ._models_py3 import SiteAuthSettings
    from ._models_py3 import SiteCloneability
    from ._models_py3 import SiteCloneabilityCriterion
    from ._models_py3 import SiteConfig
    from ._models_py3 import SiteConfigResource
    from ._models_py3 import SiteConfigurationSnapshotInfo
    from ._models_py3 import SiteExtensionInfo
    from ._models_py3 import SiteInstance
    from ._models_py3 import SiteLimits
    from ._models_py3 import SiteLogsConfig
    from ._models_py3 import SiteMachineKey
    from ._models_py3 import SitePatchResource
    from ._models_py3 import SitePhpErrorLogFlag
    from ._models_py3 import SiteSeal
    from ._models_py3 import SiteSealRequest
    from ._models_py3 import SiteSourceControl
    from ._models_py3 import SkuCapacity
    from ._models_py3 import SkuDescription
    from ._models_py3 import SkuInfo
    from ._models_py3 import SkuInfos
    from ._models_py3 import SlotConfigNamesResource
    from ._models_py3 import SlotDifference
    from ._models_py3 import SlotSwapStatus
    from ._models_py3 import SlowRequestsBasedTrigger
    from ._models_py3 import Snapshot
    from ._models_py3 import SnapshotRecoverySource
    from ._models_py3 import SnapshotRestoreRequest
    from ._models_py3 import Solution
    from ._models_py3 import SourceControl
    from ._models_py3 import StackMajorVersion
    from ._models_py3 import StackMinorVersion
    from ._models_py3 import StampCapacity
    from ._models_py3 import StaticSiteARMResource
    from ._models_py3 import StaticSiteBuildARMResource
    from ._models_py3 import StaticSiteBuildProperties
    from ._models_py3 import StaticSiteCustomDomainOverviewARMResource
    from ._models_py3 import StaticSiteFunctionOverviewARMResource
    from ._models_py3 import StaticSitePatchResource
    from ._models_py3 import StaticSiteResetPropertiesARMResource
    from ._models_py3 import StaticSiteUserARMResource
    from ._models_py3 import StaticSiteUserInvitationRequestResource
    from ._models_py3 import StaticSiteUserInvitationResponseResource
    from ._models_py3 import StatusCodesBasedTrigger
    from ._models_py3 import StorageMigrationOptions
    from ._models_py3 import StorageMigrationResponse
    from ._models_py3 import StringDictionary
    from ._models_py3 import SwiftVirtualNetwork
    from ._models_py3 import TldLegalAgreement
    from ._models_py3 import TopLevelDomain
    from ._models_py3 import TopLevelDomainAgreementOption
    from ._models_py3 import TriggeredJobHistory
    from ._models_py3 import TriggeredJobRun
    from ._models_py3 import TriggeredWebJob
    from ._models_py3 import Usage
    from ._models_py3 import User
    from ._models_py3 import ValidateRequest
    from ._models_py3 import ValidateResponse
    from ._models_py3 import ValidateResponseError
    from ._models_py3 import VirtualApplication
    from ._models_py3 import VirtualDirectory
    from ._models_py3 import VirtualIPMapping
    from ._models_py3 import VirtualNetworkProfile
    from ._models_py3 import VnetGateway
    from ._models_py3 import VnetInfo
    from ._models_py3 import VnetParameters
    from ._models_py3 import VnetRoute
    from ._models_py3 import VnetValidationFailureDetails
    from ._models_py3 import VnetValidationTestFailure
    from ._models_py3 import WebAppCollection
    from ._models_py3 import WebJob
    from ._models_py3 import WebSiteInstanceStatus
    from ._models_py3 import WorkerPool
    from ._models_py3 import WorkerPoolResource
except (SyntaxError, ImportError):
    from ._models import AbnormalTimePeriod
    from ._models import Address
    from ._models import AddressResponse
    from ._models import AnalysisData
    from ._models import AnalysisDefinition
    from ._models import ApiDefinitionInfo
    from ._models import ApiKVReference
    from ._models import ApiManagementConfig
    from ._models import ApplicationLogsConfig
    from ._models import ApplicationStack
    from ._models import ApplicationStackResource
    from ._models import AppServiceCertificate
    from ._models import AppServiceCertificateOrder
    from ._models import AppServiceCertificateOrderPatchResource
    from ._models import AppServiceCertificatePatchResource
    from ._models import AppServiceCertificateResource
    from ._models import AppServiceEnvironment
    from ._models import AppServiceEnvironmentPatchResource
    from ._models import AppServiceEnvironmentResource
    from ._models import AppServicePlan
    from ._models import AppServicePlanPatchResource
    from ._models import ArmIdWrapper
    from ._models import AutoHealActions
    from ._models import AutoHealCustomAction
    from ._models import AutoHealRules
    from ._models import AutoHealTriggers
    from ._models import AzureBlobStorageApplicationLogsConfig
    from ._models import AzureBlobStorageHttpLogsConfig
    from ._models import AzureStorageInfoValue
    from ._models import AzureStoragePropertyDictionaryResource
    from ._models import AzureTableStorageApplicationLogsConfig
    from ._models import BackupItem
    from ._models import BackupRequest
    from ._models import BackupSchedule
    from ._models import BillingMeter
    from ._models import Capability
    from ._models import Certificate
    from ._models import CertificateDetails
    from ._models import CertificateEmail
    from ._models import CertificateOrderAction
    from ._models import CertificatePatchResource
    from ._models import CloningInfo
    from ._models import ConnectionStringDictionary
    from ._models import ConnStringInfo
    from ._models import ConnStringValueTypePair
    from ._models import Contact
    from ._models import ContainerCpuStatistics
    from ._models import ContainerCpuUsage
    from ._models import ContainerInfo
    from ._models import ContainerMemoryStatistics
    from ._models import ContainerNetworkInterfaceStatistics
    from ._models import ContainerThrottlingData
    from ._models import ContinuousWebJob
    from ._models import CorsSettings
    from ._models import CsmCopySlotEntity
    from ._models import CsmMoveResourceEnvelope
    from ._models import CsmOperationDescription
    from ._models import CsmOperationDescriptionProperties
    from ._models import CsmOperationDisplay
    from ._models import CsmPublishingProfileOptions
    from ._models import CsmSlotEntity
    from ._models import CsmUsageQuota
    from ._models import CustomHostnameAnalysisResult
    from ._models import DatabaseBackupSetting
    from ._models import DataSource
    from ._models import DataTableResponseColumn
    from ._models import DataTableResponseObject
    from ._models import DefaultErrorResponse, DefaultErrorResponseException
    from ._models import DefaultErrorResponseError
    from ._models import DefaultErrorResponseErrorDetailsItem
    from ._models import DeletedAppRestoreRequest
    from ._models import DeletedSite
    from ._models import Deployment
    from ._models import DeploymentLocations
    from ._models import DetectorAbnormalTimePeriod
    from ._models import DetectorDefinition
    from ._models import DetectorInfo
    from ._models import DetectorResponse
    from ._models import DiagnosticAnalysis
    from ._models import DiagnosticCategory
    from ._models import DiagnosticData
    from ._models import DiagnosticDetectorResponse
    from ._models import DiagnosticMetricSample
    from ._models import DiagnosticMetricSet
    from ._models import Dimension
    from ._models import Domain
    from ._models import DomainAvailabilityCheckResult
    from ._models import DomainControlCenterSsoRequest
    from ._models import DomainOwnershipIdentifier
    from ._models import DomainPatchResource
    from ._models import DomainPurchaseConsent
    from ._models import DomainRecommendationSearchParameters
    from ._models import EnabledConfig
    from ._models import EndpointDependency
    from ._models import EndpointDetail
    from ._models import ErrorEntity
    from ._models import Experiments
    from ._models import FileSystemApplicationLogsConfig
    from ._models import FileSystemHttpLogsConfig
    from ._models import FunctionEnvelope
    from ._models import FunctionSecrets
    from ._models import GeoRegion
    from ._models import GlobalCsmSkuDescription
    from ._models import HandlerMapping
    from ._models import HostingEnvironmentDeploymentInfo
    from ._models import HostingEnvironmentDiagnostics
    from ._models import HostingEnvironmentProfile
    from ._models import HostKeys
    from ._models import HostName
    from ._models import HostNameBinding
    from ._models import HostNameSslState
    from ._models import HttpLogsConfig
    from ._models import HybridConnection
    from ._models import HybridConnectionKey
    from ._models import HybridConnectionLimits
    from ._models import Identifier
    from ._models import InboundEnvironmentEndpoint
    from ._models import IpSecurityRestriction
    from ._models import KeyInfo
    from ._models import KeyVaultReferenceCollection
    from ._models import KeyVaultReferenceResource
    from ._models import LocalizableString
    from ._models import LogSpecification
    from ._models import ManagedServiceIdentity
    from ._models import ManagedServiceIdentityUserAssignedIdentitiesValue
    from ._models import MetricAvailability
    from ._models import MetricSpecification
    from ._models import MigrateMySqlRequest
    from ._models import MigrateMySqlStatus
    from ._models import MSDeploy
    from ._models import MSDeployLog
    from ._models import MSDeployLogEntry
    from ._models import MSDeployStatus
    from ._models import NameIdentifier
    from ._models import NameValuePair
    from ._models import NetworkAccessControlEntry
    from ._models import NetworkFeatures
    from ._models import NetworkTrace
    from ._models import Operation
    from ._models import OutboundEnvironmentEndpoint
    from ._models import PerfMonResponse
    from ._models import PerfMonSample
    from ._models import PerfMonSet
    from ._models import PremierAddOn
    from ._models import PremierAddOnOffer
    from ._models import PremierAddOnPatchResource
    from ._models import PrivateAccess
    from ._models import PrivateAccessSubnet
    from ._models import PrivateAccessVirtualNetwork
    from ._models import PrivateEndpointConnectionResource
    from ._models import PrivateLinkConnectionApprovalRequestResource
    from ._models import PrivateLinkConnectionState
    from ._models import PrivateLinkResource
    from ._models import PrivateLinkResourceProperties
    from ._models import PrivateLinkResourcesWrapper
    from ._models import ProcessInfo
    from ._models import ProcessModuleInfo
    from ._models import ProcessThreadInfo
    from ._models import ProxyOnlyResource
    from ._models import PublicCertificate
    from ._models import PushSettings
    from ._models import RampUpRule
    from ._models import Recommendation
    from ._models import RecommendationRule
    from ._models import ReissueCertificateOrderRequest
    from ._models import RelayServiceConnectionEntity
    from ._models import Rendering
    from ._models import RenewCertificateOrderRequest
    from ._models import RequestsBasedTrigger
    from ._models import Resource
    from ._models import ResourceHealthMetadata
    from ._models import ResourceMetricAvailability
    from ._models import ResourceMetricDefinition
    from ._models import ResourceNameAvailability
    from ._models import ResourceNameAvailabilityRequest
    from ._models import ResponseMetaData
    from ._models import RestoreRequest
    from ._models import ServiceSpecification
    from ._models import Site
    from ._models import SiteAuthSettings
    from ._models import SiteCloneability
    from ._models import SiteCloneabilityCriterion
    from ._models import SiteConfig
    from ._models import SiteConfigResource
    from ._models import SiteConfigurationSnapshotInfo
    from ._models import SiteExtensionInfo
    from ._models import SiteInstance
    from ._models import SiteLimits
    from ._models import SiteLogsConfig
    from ._models import SiteMachineKey
    from ._models import SitePatchResource
    from ._models import SitePhpErrorLogFlag
    from ._models import SiteSeal
    from ._models import SiteSealRequest
    from ._models import SiteSourceControl
    from ._models import SkuCapacity
    from ._models import SkuDescription
    from ._models import SkuInfo
    from ._models import SkuInfos
    from ._models import SlotConfigNamesResource
    from ._models import SlotDifference
    from ._models import SlotSwapStatus
    from ._models import SlowRequestsBasedTrigger
    from ._models import Snapshot
    from ._models import SnapshotRecoverySource
    from ._models import SnapshotRestoreRequest
    from ._models import Solution
    from ._models import SourceControl
    from ._models import StackMajorVersion
    from ._models import StackMinorVersion
    from ._models import StampCapacity
    from ._models import StaticSiteARMResource
    from ._models import StaticSiteBuildARMResource
    from ._models import StaticSiteBuildProperties
    from ._models import StaticSiteCustomDomainOverviewARMResource
    from ._models import StaticSiteFunctionOverviewARMResource
    from ._models import StaticSitePatchResource
    from ._models import StaticSiteResetPropertiesARMResource
    from ._models import StaticSiteUserARMResource
    from ._models import StaticSiteUserInvitationRequestResource
    from ._models import StaticSiteUserInvitationResponseResource
    from ._models import StatusCodesBasedTrigger
    from ._models import StorageMigrationOptions
    from ._models import StorageMigrationResponse
    from ._models import StringDictionary
    from ._models import SwiftVirtualNetwork
    from ._models import TldLegalAgreement
    from ._models import TopLevelDomain
    from ._models import TopLevelDomainAgreementOption
    from ._models import TriggeredJobHistory
    from ._models import TriggeredJobRun
    from ._models import TriggeredWebJob
    from ._models import Usage
    from ._models import User
    from ._models import ValidateRequest
    from ._models import ValidateResponse
    from ._models import ValidateResponseError
    from ._models import VirtualApplication
    from ._models import VirtualDirectory
    from ._models import VirtualIPMapping
    from ._models import VirtualNetworkProfile
    from ._models import VnetGateway
    from ._models import VnetInfo
    from ._models import VnetParameters
    from ._models import VnetRoute
    from ._models import VnetValidationFailureDetails
    from ._models import VnetValidationTestFailure
    from ._models import WebAppCollection
    from ._models import WebJob
    from ._models import WebSiteInstanceStatus
    from ._models import WorkerPool
    from ._models import WorkerPoolResource
from ._paged_models import AnalysisDefinitionPaged
from ._paged_models import ApplicationStackResourcePaged
from ._paged_models import AppServiceCertificateOrderPaged
from ._paged_models import AppServiceCertificateResourcePaged
from ._paged_models import AppServiceEnvironmentResourcePaged
from ._paged_models import AppServicePlanPaged
from ._paged_models import BackupItemPaged
from ._paged_models import BillingMeterPaged
from ._paged_models import CertificatePaged
from ._paged_models import ContinuousWebJobPaged
from ._paged_models import CsmOperationDescriptionPaged
from ._paged_models import CsmUsageQuotaPaged
from ._paged_models import DeletedSitePaged
from ._paged_models import DeploymentPaged
from ._paged_models import DetectorDefinitionPaged
from ._paged_models import DetectorResponsePaged
from ._paged_models import DiagnosticCategoryPaged
from ._paged_models import DomainOwnershipIdentifierPaged
from ._paged_models import DomainPaged
from ._paged_models import FunctionEnvelopePaged
from ._paged_models import GeoRegionPaged
from ._paged_models import HostNameBindingPaged
from ._paged_models import HybridConnectionPaged
from ._paged_models import IdentifierPaged
from ._paged_models import InboundEnvironmentEndpointPaged
from ._paged_models import NameIdentifierPaged
from ._paged_models import OutboundEnvironmentEndpointPaged
from ._paged_models import PerfMonResponsePaged
from ._paged_models import PremierAddOnOfferPaged
from ._paged_models import ProcessInfoPaged
from ._paged_models import ProcessModuleInfoPaged
from ._paged_models import ProcessThreadInfoPaged
from ._paged_models import PublicCertificatePaged
from ._paged_models import RecommendationPaged
from ._paged_models import ResourceHealthMetadataPaged
from ._paged_models import ResourceMetricDefinitionPaged
from ._paged_models import SiteConfigResourcePaged
from ._paged_models import SiteConfigurationSnapshotInfoPaged
from ._paged_models import SiteExtensionInfoPaged
from ._paged_models import SiteInstancePaged
from ._paged_models import SitePaged
from ._paged_models import SkuInfoPaged
from ._paged_models import SlotDifferencePaged
from ._paged_models import SnapshotPaged
from ._paged_models import SourceControlPaged
from ._paged_models import StampCapacityPaged
from ._paged_models import StaticSiteARMResourcePaged
from ._paged_models import StaticSiteBuildARMResourcePaged
from ._paged_models import StaticSiteCustomDomainOverviewARMResourcePaged
from ._paged_models import StaticSiteFunctionOverviewARMResourcePaged
from ._paged_models import StaticSiteUserARMResourcePaged
from ._paged_models import StrPaged
from ._paged_models import TldLegalAgreementPaged
from ._paged_models import TopLevelDomainPaged
from ._paged_models import TriggeredJobHistoryPaged
from ._paged_models import TriggeredWebJobPaged
from ._paged_models import UsagePaged
from ._paged_models import WebJobPaged
from ._paged_models import WorkerPoolResourcePaged
from ._web_site_management_client_enums import (
    KeyVaultSecretStatus,
    CertificateProductType,
    ProvisioningState,
    CertificateOrderStatus,
    CertificateOrderActionType,
    RouteType,
    ManagedServiceIdentityType,
    IpFilterTag,
    AutoHealActionType,
    ConnectionStringType,
    ScmType,
    ManagedPipelineMode,
    SiteLoadBalancing,
    SupportedTlsVersions,
    FtpsState,
    SslState,
    HostType,
    UsageState,
    SiteAvailabilityState,
    RedundancyMode,
    StatusOptions,
    DomainStatus,
    AzureResourceType,
    CustomHostNameDnsRecordType,
    HostNameType,
    DnsType,
    DomainType,
    HostingEnvironmentStatus,
    InternalLoadBalancingMode,
    ComputeModeOptions,
    WorkerSizeOptions,
    AccessControlEntryAction,
    OperationStatus,
    IssueType,
    SolutionType,
    RenderingType,
    ResourceScopeType,
    NotificationLevel,
    Channels,
    AppServicePlanRestrictions,
    InAvailabilityReasonType,
    CheckNameResourceTypes,
    ValidateResourceTypes,
    ResolveStatus,
    ConfigReferenceSource,
    ConfigReferenceLocation,
    LogLevel,
    AzureStorageType,
    AzureStorageState,
    BackupItemStatus,
    DatabaseType,
    FrequencyUnit,
    ContinuousWebJobStatus,
    WebJobType,
    PublishingProfileFormat,
    DnsVerificationTestResult,
    MSDeployLogEntryType,
    MSDeployProvisioningState,
    MySqlMigrationType,
    PublicCertificateLocation,
    BackupRestoreOperationType,
    UnauthenticatedClientAction,
    BuiltInAuthenticationProvider,
    CloneAbilityResult,
    SiteExtensionType,
    TriggeredWebJobStatus,
    SiteRuntimeState,
    BuildStatus,
    TriggerTypes,
    SkuName,
)

__all__ = [
    'AbnormalTimePeriod',
    'Address',
    'AddressResponse',
    'AnalysisData',
    'AnalysisDefinition',
    'ApiDefinitionInfo',
    'ApiKVReference',
    'ApiManagementConfig',
    'ApplicationLogsConfig',
    'ApplicationStack',
    'ApplicationStackResource',
    'AppServiceCertificate',
    'AppServiceCertificateOrder',
    'AppServiceCertificateOrderPatchResource',
    'AppServiceCertificatePatchResource',
    'AppServiceCertificateResource',
    'AppServiceEnvironment',
    'AppServiceEnvironmentPatchResource',
    'AppServiceEnvironmentResource',
    'AppServicePlan',
    'AppServicePlanPatchResource',
    'ArmIdWrapper',
    'AutoHealActions',
    'AutoHealCustomAction',
    'AutoHealRules',
    'AutoHealTriggers',
    'AzureBlobStorageApplicationLogsConfig',
    'AzureBlobStorageHttpLogsConfig',
    'AzureStorageInfoValue',
    'AzureStoragePropertyDictionaryResource',
    'AzureTableStorageApplicationLogsConfig',
    'BackupItem',
    'BackupRequest',
    'BackupSchedule',
    'BillingMeter',
    'Capability',
    'Certificate',
    'CertificateDetails',
    'CertificateEmail',
    'CertificateOrderAction',
    'CertificatePatchResource',
    'CloningInfo',
    'ConnectionStringDictionary',
    'ConnStringInfo',
    'ConnStringValueTypePair',
    'Contact',
    'ContainerCpuStatistics',
    'ContainerCpuUsage',
    'ContainerInfo',
    'ContainerMemoryStatistics',
    'ContainerNetworkInterfaceStatistics',
    'ContainerThrottlingData',
    'ContinuousWebJob',
    'CorsSettings',
    'CsmCopySlotEntity',
    'CsmMoveResourceEnvelope',
    'CsmOperationDescription',
    'CsmOperationDescriptionProperties',
    'CsmOperationDisplay',
    'CsmPublishingProfileOptions',
    'CsmSlotEntity',
    'CsmUsageQuota',
    'CustomHostnameAnalysisResult',
    'DatabaseBackupSetting',
    'DataSource',
    'DataTableResponseColumn',
    'DataTableResponseObject',
    'DefaultErrorResponse', 'DefaultErrorResponseException',
    'DefaultErrorResponseError',
    'DefaultErrorResponseErrorDetailsItem',
    'DeletedAppRestoreRequest',
    'DeletedSite',
    'Deployment',
    'DeploymentLocations',
    'DetectorAbnormalTimePeriod',
    'DetectorDefinition',
    'DetectorInfo',
    'DetectorResponse',
    'DiagnosticAnalysis',
    'DiagnosticCategory',
    'DiagnosticData',
    'DiagnosticDetectorResponse',
    'DiagnosticMetricSample',
    'DiagnosticMetricSet',
    'Dimension',
    'Domain',
    'DomainAvailabilityCheckResult',
    'DomainControlCenterSsoRequest',
    'DomainOwnershipIdentifier',
    'DomainPatchResource',
    'DomainPurchaseConsent',
    'DomainRecommendationSearchParameters',
    'EnabledConfig',
    'EndpointDependency',
    'EndpointDetail',
    'ErrorEntity',
    'Experiments',
    'FileSystemApplicationLogsConfig',
    'FileSystemHttpLogsConfig',
    'FunctionEnvelope',
    'FunctionSecrets',
    'GeoRegion',
    'GlobalCsmSkuDescription',
    'HandlerMapping',
    'HostingEnvironmentDeploymentInfo',
    'HostingEnvironmentDiagnostics',
    'HostingEnvironmentProfile',
    'HostKeys',
    'HostName',
    'HostNameBinding',
    'HostNameSslState',
    'HttpLogsConfig',
    'HybridConnection',
    'HybridConnectionKey',
    'HybridConnectionLimits',
    'Identifier',
    'InboundEnvironmentEndpoint',
    'IpSecurityRestriction',
    'KeyInfo',
    'KeyVaultReferenceCollection',
    'KeyVaultReferenceResource',
    'LocalizableString',
    'LogSpecification',
    'ManagedServiceIdentity',
    'ManagedServiceIdentityUserAssignedIdentitiesValue',
    'MetricAvailability',
    'MetricSpecification',
    'MigrateMySqlRequest',
    'MigrateMySqlStatus',
    'MSDeploy',
    'MSDeployLog',
    'MSDeployLogEntry',
    'MSDeployStatus',
    'NameIdentifier',
    'NameValuePair',
    'NetworkAccessControlEntry',
    'NetworkFeatures',
    'NetworkTrace',
    'Operation',
    'OutboundEnvironmentEndpoint',
    'PerfMonResponse',
    'PerfMonSample',
    'PerfMonSet',
    'PremierAddOn',
    'PremierAddOnOffer',
    'PremierAddOnPatchResource',
    'PrivateAccess',
    'PrivateAccessSubnet',
    'PrivateAccessVirtualNetwork',
    'PrivateEndpointConnectionResource',
    'PrivateLinkConnectionApprovalRequestResource',
    'PrivateLinkConnectionState',
    'PrivateLinkResource',
    'PrivateLinkResourceProperties',
    'PrivateLinkResourcesWrapper',
    'ProcessInfo',
    'ProcessModuleInfo',
    'ProcessThreadInfo',
    'ProxyOnlyResource',
    'PublicCertificate',
    'PushSettings',
    'RampUpRule',
    'Recommendation',
    'RecommendationRule',
    'ReissueCertificateOrderRequest',
    'RelayServiceConnectionEntity',
    'Rendering',
    'RenewCertificateOrderRequest',
    'RequestsBasedTrigger',
    'Resource',
    'ResourceHealthMetadata',
    'ResourceMetricAvailability',
    'ResourceMetricDefinition',
    'ResourceNameAvailability',
    'ResourceNameAvailabilityRequest',
    'ResponseMetaData',
    'RestoreRequest',
    'ServiceSpecification',
    'Site',
    'SiteAuthSettings',
    'SiteCloneability',
    'SiteCloneabilityCriterion',
    'SiteConfig',
    'SiteConfigResource',
    'SiteConfigurationSnapshotInfo',
    'SiteExtensionInfo',
    'SiteInstance',
    'SiteLimits',
    'SiteLogsConfig',
    'SiteMachineKey',
    'SitePatchResource',
    'SitePhpErrorLogFlag',
    'SiteSeal',
    'SiteSealRequest',
    'SiteSourceControl',
    'SkuCapacity',
    'SkuDescription',
    'SkuInfo',
    'SkuInfos',
    'SlotConfigNamesResource',
    'SlotDifference',
    'SlotSwapStatus',
    'SlowRequestsBasedTrigger',
    'Snapshot',
    'SnapshotRecoverySource',
    'SnapshotRestoreRequest',
    'Solution',
    'SourceControl',
    'StackMajorVersion',
    'StackMinorVersion',
    'StampCapacity',
    'StaticSiteARMResource',
    'StaticSiteBuildARMResource',
    'StaticSiteBuildProperties',
    'StaticSiteCustomDomainOverviewARMResource',
    'StaticSiteFunctionOverviewARMResource',
    'StaticSitePatchResource',
    'StaticSiteResetPropertiesARMResource',
    'StaticSiteUserARMResource',
    'StaticSiteUserInvitationRequestResource',
    'StaticSiteUserInvitationResponseResource',
    'StatusCodesBasedTrigger',
    'StorageMigrationOptions',
    'StorageMigrationResponse',
    'StringDictionary',
    'SwiftVirtualNetwork',
    'TldLegalAgreement',
    'TopLevelDomain',
    'TopLevelDomainAgreementOption',
    'TriggeredJobHistory',
    'TriggeredJobRun',
    'TriggeredWebJob',
    'Usage',
    'User',
    'ValidateRequest',
    'ValidateResponse',
    'ValidateResponseError',
    'VirtualApplication',
    'VirtualDirectory',
    'VirtualIPMapping',
    'VirtualNetworkProfile',
    'VnetGateway',
    'VnetInfo',
    'VnetParameters',
    'VnetRoute',
    'VnetValidationFailureDetails',
    'VnetValidationTestFailure',
    'WebAppCollection',
    'WebJob',
    'WebSiteInstanceStatus',
    'WorkerPool',
    'WorkerPoolResource',
    'AppServiceCertificateOrderPaged',
    'AppServiceCertificateResourcePaged',
    'CsmOperationDescriptionPaged',
    'DomainPaged',
    'NameIdentifierPaged',
    'DomainOwnershipIdentifierPaged',
    'TopLevelDomainPaged',
    'TldLegalAgreementPaged',
    'CertificatePaged',
    'DeletedSitePaged',
    'DetectorResponsePaged',
    'DiagnosticCategoryPaged',
    'AnalysisDefinitionPaged',
    'DetectorDefinitionPaged',
    'ApplicationStackResourcePaged',
    'RecommendationPaged',
    'SourceControlPaged',
    'BillingMeterPaged',
    'GeoRegionPaged',
    'IdentifierPaged',
    'PremierAddOnOfferPaged',
    'SitePaged',
    'BackupItemPaged',
    'SiteConfigResourcePaged',
    'SiteConfigurationSnapshotInfoPaged',
    'ContinuousWebJobPaged',
    'DeploymentPaged',
    'FunctionEnvelopePaged',
    'HostNameBindingPaged',
    'SiteInstancePaged',
    'ProcessInfoPaged',
    'ProcessModuleInfoPaged',
    'ProcessThreadInfoPaged',
    'PerfMonResponsePaged',
    'PublicCertificatePaged',
    'SiteExtensionInfoPaged',
    'SlotDifferencePaged',
    'SnapshotPaged',
    'TriggeredWebJobPaged',
    'TriggeredJobHistoryPaged',
    'CsmUsageQuotaPaged',
    'WebJobPaged',
    'StaticSiteARMResourcePaged',
    'StaticSiteUserARMResourcePaged',
    'StaticSiteBuildARMResourcePaged',
    'StaticSiteFunctionOverviewARMResourcePaged',
    'StaticSiteCustomDomainOverviewARMResourcePaged',
    'AppServiceEnvironmentResourcePaged',
    'StampCapacityPaged',
    'InboundEnvironmentEndpointPaged',
    'WorkerPoolResourcePaged',
    'ResourceMetricDefinitionPaged',
    'SkuInfoPaged',
    'UsagePaged',
    'OutboundEnvironmentEndpointPaged',
    'AppServicePlanPaged',
    'StrPaged',
    'HybridConnectionPaged',
    'ResourceHealthMetadataPaged',
    'KeyVaultSecretStatus',
    'CertificateProductType',
    'ProvisioningState',
    'CertificateOrderStatus',
    'CertificateOrderActionType',
    'RouteType',
    'ManagedServiceIdentityType',
    'IpFilterTag',
    'AutoHealActionType',
    'ConnectionStringType',
    'ScmType',
    'ManagedPipelineMode',
    'SiteLoadBalancing',
    'SupportedTlsVersions',
    'FtpsState',
    'SslState',
    'HostType',
    'UsageState',
    'SiteAvailabilityState',
    'RedundancyMode',
    'StatusOptions',
    'DomainStatus',
    'AzureResourceType',
    'CustomHostNameDnsRecordType',
    'HostNameType',
    'DnsType',
    'DomainType',
    'HostingEnvironmentStatus',
    'InternalLoadBalancingMode',
    'ComputeModeOptions',
    'WorkerSizeOptions',
    'AccessControlEntryAction',
    'OperationStatus',
    'IssueType',
    'SolutionType',
    'RenderingType',
    'ResourceScopeType',
    'NotificationLevel',
    'Channels',
    'AppServicePlanRestrictions',
    'InAvailabilityReasonType',
    'CheckNameResourceTypes',
    'ValidateResourceTypes',
    'ResolveStatus',
    'ConfigReferenceSource',
    'ConfigReferenceLocation',
    'LogLevel',
    'AzureStorageType',
    'AzureStorageState',
    'BackupItemStatus',
    'DatabaseType',
    'FrequencyUnit',
    'ContinuousWebJobStatus',
    'WebJobType',
    'PublishingProfileFormat',
    'DnsVerificationTestResult',
    'MSDeployLogEntryType',
    'MSDeployProvisioningState',
    'MySqlMigrationType',
    'PublicCertificateLocation',
    'BackupRestoreOperationType',
    'UnauthenticatedClientAction',
    'BuiltInAuthenticationProvider',
    'CloneAbilityResult',
    'SiteExtensionType',
    'TriggeredWebJobStatus',
    'SiteRuntimeState',
    'BuildStatus',
    'TriggerTypes',
    'SkuName',
]