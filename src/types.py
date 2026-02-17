from typing import TypedDict, List, Optional


class VehicleLocationDict(TypedDict):
    Longitude: str
    Latitude: str


class FramedVehicleJourneyRefDict(TypedDict):
    DataFrameRef: str
    DatedVehicleJourneyRef: str


class MonitoredCallDict(TypedDict, total=False):
    StopPointRef: str
    StopPointName: str
    VehicleLocationAtStop: str
    VehicleAtStop: str
    DestinationDisplay: str
    AimedArrivalTime: str
    ExpectedArrivalTime: Optional[str]
    AimedDepartureTime: str
    ExpectedDepartureTime: Optional[str]
    Distances: str


class MonitoredVehicleJourneyDict(TypedDict):
    LineRef: str
    DirectionRef: str
    FramedVehicleJourneyRef: FramedVehicleJourneyRefDict
    PublishedLineName: str
    OperatorRef: str
    OriginRef: str
    OriginName: str
    DestinationRef: str
    DestinationName: str
    Monitored: bool
    InCongestion: Optional[bool]
    VehicleLocation: VehicleLocationDict
    Bearing: Optional[str]
    Occupancy: Optional[str]
    VehicleRef: str
    MonitoredCall: MonitoredCallDict


class MonitoredStopVisitDict(TypedDict):
    RecordedAtTime: str
    MonitoringRef: str
    MonitoredVehicleJourney: MonitoredVehicleJourneyDict


class StopMonitoringDeliveryDict(TypedDict):
    version: str
    ResponseTimestamp: str
    Status: bool
    MonitoredStopVisit: List[MonitoredStopVisitDict]


class ServiceDeliveryDict(TypedDict):
    ResponseTimestamp: str
    ProducerRef: str
    Status: bool
    StopMonitoringDelivery: StopMonitoringDeliveryDict


class StopMonitoringResp(TypedDict):
    ServiceDelivery: ServiceDeliveryDict
