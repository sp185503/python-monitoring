# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.protobuf import duration_pb2 as duration  # type: ignore
from google.type import calendar_period_pb2 as gt_calendar_period  # type: ignore


__protobuf__ = proto.module(
    package="google.monitoring.v3",
    manifest={
        "Service",
        "ServiceLevelObjective",
        "ServiceLevelIndicator",
        "BasicSli",
        "Range",
        "RequestBasedSli",
        "TimeSeriesRatio",
        "DistributionCut",
        "WindowsBasedSli",
    },
)


class Service(proto.Message):
    r"""A ``Service`` is a discrete, autonomous, and network-accessible
    unit, designed to solve an individual concern
    (`Wikipedia <https://en.wikipedia.org/wiki/Service-orientation>`__).
    In Cloud Monitoring, a ``Service`` acts as the root resource under
    which operational aspects of the service are accessible.

    Attributes:
        name (str):
            Resource name for this Service. The format is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]
        display_name (str):
            Name used for UI elements listing this
            Service.
        custom (~.gm_service.Service.Custom):
            Custom service type.
        app_engine (~.gm_service.Service.AppEngine):
            Type used for App Engine services.
        cloud_endpoints (~.gm_service.Service.CloudEndpoints):
            Type used for Cloud Endpoints services.
        cluster_istio (~.gm_service.Service.ClusterIstio):
            Type used for Istio services that live in a
            Kubernetes cluster.
        mesh_istio (~.gm_service.Service.MeshIstio):
            Type used for Istio services scoped to an
            Istio mesh.
        telemetry (~.gm_service.Service.Telemetry):
            Configuration for how to query telemetry on a
            Service.
    """

    class Custom(proto.Message):
        r"""Custom view of service telemetry. Currently a place-holder
        pending final design.
        """

    class AppEngine(proto.Message):
        r"""App Engine service. Learn more at
        https://cloud.google.com/appengine.

        Attributes:
            module_id (str):
                The ID of the App Engine module underlying this service.
                Corresponds to the ``module_id`` resource label in the
                ``gae_app`` monitored resource:
                https://cloud.google.com/monitoring/api/resources#tag_gae_app
        """

        module_id = proto.Field(proto.STRING, number=1)

    class CloudEndpoints(proto.Message):
        r"""Cloud Endpoints service. Learn more at
        https://cloud.google.com/endpoints.

        Attributes:
            service (str):
                The name of the Cloud Endpoints service underlying this
                service. Corresponds to the ``service`` resource label in
                the ``api`` monitored resource:
                https://cloud.google.com/monitoring/api/resources#tag_api
        """

        service = proto.Field(proto.STRING, number=1)

    class ClusterIstio(proto.Message):
        r"""Istio service scoped to a single Kubernetes cluster. Learn
        more at http://istio.io.

        Attributes:
            location (str):
                The location of the Kubernetes cluster in which this Istio
                service is defined. Corresponds to the ``location`` resource
                label in ``k8s_cluster`` resources.
            cluster_name (str):
                The name of the Kubernetes cluster in which this Istio
                service is defined. Corresponds to the ``cluster_name``
                resource label in ``k8s_cluster`` resources.
            service_namespace (str):
                The namespace of the Istio service underlying this service.
                Corresponds to the ``destination_service_namespace`` metric
                label in Istio metrics.
            service_name (str):
                The name of the Istio service underlying this service.
                Corresponds to the ``destination_service_name`` metric label
                in Istio metrics.
        """

        location = proto.Field(proto.STRING, number=1)

        cluster_name = proto.Field(proto.STRING, number=2)

        service_namespace = proto.Field(proto.STRING, number=3)

        service_name = proto.Field(proto.STRING, number=4)

    class MeshIstio(proto.Message):
        r"""Istio service scoped to an Istio mesh

        Attributes:
            mesh_uid (str):
                Identifier for the mesh in which this Istio service is
                defined. Corresponds to the ``mesh_uid`` metric label in
                Istio metrics.
            service_namespace (str):
                The namespace of the Istio service underlying this service.
                Corresponds to the ``destination_service_namespace`` metric
                label in Istio metrics.
            service_name (str):
                The name of the Istio service underlying this service.
                Corresponds to the ``destination_service_name`` metric label
                in Istio metrics.
        """

        mesh_uid = proto.Field(proto.STRING, number=1)

        service_namespace = proto.Field(proto.STRING, number=3)

        service_name = proto.Field(proto.STRING, number=4)

    class Telemetry(proto.Message):
        r"""Configuration for how to query telemetry on a Service.

        Attributes:
            resource_name (str):
                The full name of the resource that defines this service.
                Formatted as described in
                https://cloud.google.com/apis/design/resource_names.
        """

        resource_name = proto.Field(proto.STRING, number=1)

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    custom = proto.Field(proto.MESSAGE, number=6, oneof="identifier", message=Custom,)

    app_engine = proto.Field(
        proto.MESSAGE, number=7, oneof="identifier", message=AppEngine,
    )

    cloud_endpoints = proto.Field(
        proto.MESSAGE, number=8, oneof="identifier", message=CloudEndpoints,
    )

    cluster_istio = proto.Field(
        proto.MESSAGE, number=9, oneof="identifier", message=ClusterIstio,
    )

    mesh_istio = proto.Field(
        proto.MESSAGE, number=10, oneof="identifier", message=MeshIstio,
    )

    telemetry = proto.Field(proto.MESSAGE, number=13, message=Telemetry,)


class ServiceLevelObjective(proto.Message):
    r"""A Service-Level Objective (SLO) describes a level of desired
    good service. It consists of a service-level indicator (SLI), a
    performance goal, and a period over which the objective is to be
    evaluated against that goal. The SLO can use SLIs defined in a
    number of different manners. Typical SLOs might include "99% of
    requests in each rolling week have latency below 200
    milliseconds" or "99.5% of requests in each calendar month
    return successfully."

    Attributes:
        name (str):
            Resource name for this ``ServiceLevelObjective``. The format
            is:

            ::

                projects/[PROJECT_ID_OR_NUMBER]/services/[SERVICE_ID]/serviceLevelObjectives/[SLO_NAME]
        display_name (str):
            Name used for UI elements listing this SLO.
        service_level_indicator (~.gm_service.ServiceLevelIndicator):
            The definition of good service, used to measure and
            calculate the quality of the ``Service``'s performance with
            respect to a single aspect of service quality.
        goal (float):
            The fraction of service that must be good in order for this
            objective to be met. ``0 < goal <= 0.999``.
        rolling_period (~.duration.Duration):
            A rolling time period, semantically "in the past
            ``<rolling_period>``". Must be an integer multiple of 1 day
            no larger than 30 days.
        calendar_period (~.gt_calendar_period.CalendarPeriod):
            A calendar period, semantically "since the start of the
            current ``<calendar_period>``". At this time, only ``DAY``,
            ``WEEK``, ``FORTNIGHT``, and ``MONTH`` are supported.
    """

    class View(proto.Enum):
        r"""``ServiceLevelObjective.View`` determines what form of
        ``ServiceLevelObjective`` is returned from
        ``GetServiceLevelObjective``, ``ListServiceLevelObjectives``, and
        ``ListServiceLevelObjectiveVersions`` RPCs.
        """
        VIEW_UNSPECIFIED = 0
        FULL = 2
        EXPLICIT = 1

    name = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=11)

    service_level_indicator = proto.Field(
        proto.MESSAGE, number=3, message="ServiceLevelIndicator",
    )

    goal = proto.Field(proto.DOUBLE, number=4)

    rolling_period = proto.Field(
        proto.MESSAGE, number=5, oneof="period", message=duration.Duration,
    )

    calendar_period = proto.Field(
        proto.ENUM, number=6, oneof="period", enum=gt_calendar_period.CalendarPeriod,
    )


class ServiceLevelIndicator(proto.Message):
    r"""A Service-Level Indicator (SLI) describes the "performance" of a
    service. For some services, the SLI is well-defined. In such cases,
    the SLI can be described easily by referencing the well-known SLI
    and providing the needed parameters. Alternatively, a "custom" SLI
    can be defined with a query to the underlying metric store. An SLI
    is defined to be ``good_service / total_service`` over any queried
    time interval. The value of performance always falls into the range
    ``0 <= performance <= 1``. A custom SLI describes how to compute
    this ratio, whether this is by dividing values from a pair of time
    series, cutting a ``Distribution`` into good and bad counts, or
    counting time windows in which the service complies with a
    criterion. For separation of concerns, a single Service-Level
    Indicator measures performance for only one aspect of service
    quality, such as fraction of successful queries or fast-enough
    queries.

    Attributes:
        basic_sli (~.gm_service.BasicSli):
            Basic SLI on a well-known service type.
        request_based (~.gm_service.RequestBasedSli):
            Request-based SLIs
        windows_based (~.gm_service.WindowsBasedSli):
            Windows-based SLIs
    """

    basic_sli = proto.Field(proto.MESSAGE, number=4, oneof="type", message="BasicSli",)

    request_based = proto.Field(
        proto.MESSAGE, number=1, oneof="type", message="RequestBasedSli",
    )

    windows_based = proto.Field(
        proto.MESSAGE, number=2, oneof="type", message="WindowsBasedSli",
    )


class BasicSli(proto.Message):
    r"""An SLI measuring performance on a well-known service type.
    Performance will be computed on the basis of pre-defined metrics.
    The type of the ``service_resource`` determines the metrics to use
    and the ``service_resource.labels`` and ``metric_labels`` are used
    to construct a monitoring filter to filter that metric down to just
    the data relevant to this service.

    Attributes:
        method (Sequence[str]):
            OPTIONAL: The set of RPCs to which this SLI
            is relevant. Telemetry from other methods will
            not be used to calculate performance for this
            SLI. If omitted, this SLI applies to all the
            Service's methods. For service types that don't
            support breaking down by method, setting this
            field will result in an error.
        location (Sequence[str]):
            OPTIONAL: The set of locations to which this
            SLI is relevant. Telemetry from other locations
            will not be used to calculate performance for
            this SLI. If omitted, this SLI applies to all
            locations in which the Service has activity. For
            service types that don't support breaking down
            by location, setting this field will result in
            an error.
        version (Sequence[str]):
            OPTIONAL: The set of API versions to which
            this SLI is relevant. Telemetry from other API
            versions will not be used to calculate
            performance for this SLI. If omitted, this SLI
            applies to all API versions. For service types
            that don't support breaking down by version,
            setting this field will result in an error.
        availability (~.gm_service.BasicSli.AvailabilityCriteria):
            Good service is defined to be the count of
            requests made to this service that return
            successfully.
        latency (~.gm_service.BasicSli.LatencyCriteria):
            Good service is defined to be the count of requests made to
            this service that are fast enough with respect to
            ``latency.threshold``.
    """

    class AvailabilityCriteria(proto.Message):
        r"""Future parameters for the availability SLI."""

    class LatencyCriteria(proto.Message):
        r"""Parameters for a latency threshold SLI.

        Attributes:
            threshold (~.duration.Duration):
                Good service is defined to be the count of requests made to
                this service that return in no more than ``threshold``.
        """

        threshold = proto.Field(proto.MESSAGE, number=3, message=duration.Duration,)

    method = proto.RepeatedField(proto.STRING, number=7)

    location = proto.RepeatedField(proto.STRING, number=8)

    version = proto.RepeatedField(proto.STRING, number=9)

    availability = proto.Field(
        proto.MESSAGE, number=2, oneof="sli_criteria", message=AvailabilityCriteria,
    )

    latency = proto.Field(
        proto.MESSAGE, number=3, oneof="sli_criteria", message=LatencyCriteria,
    )


class Range(proto.Message):
    r"""Range of numerical values, inclusive of ``min`` and exclusive of
    ``max``. If the open range "< range.max" is desired, set
    ``range.min = -infinity``. If the open range ">= range.min" is
    desired, set ``range.max = infinity``.

    Attributes:
        min_ (float):
            Range minimum.
        max_ (float):
            Range maximum.
    """

    min_ = proto.Field(proto.DOUBLE, number=1)

    max_ = proto.Field(proto.DOUBLE, number=2)


class RequestBasedSli(proto.Message):
    r"""Service Level Indicators for which atomic units of service
    are counted directly.

    Attributes:
        good_total_ratio (~.gm_service.TimeSeriesRatio):
            ``good_total_ratio`` is used when the ratio of
            ``good_service`` to ``total_service`` is computed from two
            ``TimeSeries``.
        distribution_cut (~.gm_service.DistributionCut):
            ``distribution_cut`` is used when ``good_service`` is a
            count of values aggregated in a ``Distribution`` that fall
            into a good range. The ``total_service`` is the total count
            of all values aggregated in the ``Distribution``.
    """

    good_total_ratio = proto.Field(
        proto.MESSAGE, number=1, oneof="method", message="TimeSeriesRatio",
    )

    distribution_cut = proto.Field(
        proto.MESSAGE, number=3, oneof="method", message="DistributionCut",
    )


class TimeSeriesRatio(proto.Message):
    r"""A ``TimeSeriesRatio`` specifies two ``TimeSeries`` to use for
    computing the ``good_service / total_service`` ratio. The specified
    ``TimeSeries`` must have ``ValueType = DOUBLE`` or
    ``ValueType = INT64`` and must have ``MetricKind = DELTA`` or
    ``MetricKind = CUMULATIVE``. The ``TimeSeriesRatio`` must specify
    exactly two of good, bad, and total, and the relationship
    ``good_service + bad_service = total_service`` will be assumed.

    Attributes:
        good_service_filter (str):
            A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifying a ``TimeSeries`` quantifying good service
            provided. Must have ``ValueType = DOUBLE`` or
            ``ValueType = INT64`` and must have ``MetricKind = DELTA``
            or ``MetricKind = CUMULATIVE``.
        bad_service_filter (str):
            A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifying a ``TimeSeries`` quantifying bad service, either
            demanded service that was not provided or demanded service
            that was of inadequate quality. Must have
            ``ValueType = DOUBLE`` or ``ValueType = INT64`` and must
            have ``MetricKind = DELTA`` or ``MetricKind = CUMULATIVE``.
        total_service_filter (str):
            A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifying a ``TimeSeries`` quantifying total demanded
            service. Must have ``ValueType = DOUBLE`` or
            ``ValueType = INT64`` and must have ``MetricKind = DELTA``
            or ``MetricKind = CUMULATIVE``.
    """

    good_service_filter = proto.Field(proto.STRING, number=4)

    bad_service_filter = proto.Field(proto.STRING, number=5)

    total_service_filter = proto.Field(proto.STRING, number=6)


class DistributionCut(proto.Message):
    r"""A ``DistributionCut`` defines a ``TimeSeries`` and thresholds used
    for measuring good service and total service. The ``TimeSeries``
    must have ``ValueType = DISTRIBUTION`` and ``MetricKind = DELTA`` or
    ``MetricKind = CUMULATIVE``. The computed ``good_service`` will be
    the count of values x in the ``Distribution`` such that
    ``range.min <= x < range.max``.

    Attributes:
        distribution_filter (str):
            A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifying a ``TimeSeries`` aggregating values. Must have
            ``ValueType = DISTRIBUTION`` and ``MetricKind = DELTA`` or
            ``MetricKind = CUMULATIVE``.
        range_ (~.gm_service.Range):
            Range of values considered "good." For a one-
            ided range, set one bound to an infinite value.
    """

    distribution_filter = proto.Field(proto.STRING, number=4)

    range_ = proto.Field(proto.MESSAGE, number=5, message=Range,)


class WindowsBasedSli(proto.Message):
    r"""A ``WindowsBasedSli`` defines ``good_service`` as the count of time
    windows for which the provided service was of good quality. Criteria
    for determining if service was good are embedded in the
    ``window_criterion``.

    Attributes:
        good_bad_metric_filter (str):
            A `monitoring
            filter <https://cloud.google.com/monitoring/api/v3/filters>`__
            specifying a ``TimeSeries`` with ``ValueType = BOOL``. The
            window is good if any ``true`` values appear in the window.
        good_total_ratio_threshold (~.gm_service.WindowsBasedSli.PerformanceThreshold):
            A window is good if its ``performance`` is high enough.
        metric_mean_in_range (~.gm_service.WindowsBasedSli.MetricRange):
            A window is good if the metric's value is in
            a good range, averaged across returned streams.
        metric_sum_in_range (~.gm_service.WindowsBasedSli.MetricRange):
            A window is good if the metric's value is in
            a good range, summed across returned streams.
        window_period (~.duration.Duration):
            Duration over which window quality is evaluated. Must be an
            integer fraction of a day and at least ``60s``.
    """

    class PerformanceThreshold(proto.Message):
        r"""A ``PerformanceThreshold`` is used when each window is good when
        that window has a sufficiently high ``performance``.

        Attributes:
            performance (~.gm_service.RequestBasedSli):
                ``RequestBasedSli`` to evaluate to judge window quality.
            basic_sli_performance (~.gm_service.BasicSli):
                ``BasicSli`` to evaluate to judge window quality.
            threshold (float):
                If window ``performance >= threshold``, the window is
                counted as good.
        """

        performance = proto.Field(
            proto.MESSAGE, number=1, oneof="type", message=RequestBasedSli,
        )

        basic_sli_performance = proto.Field(
            proto.MESSAGE, number=3, oneof="type", message=BasicSli,
        )

        threshold = proto.Field(proto.DOUBLE, number=2)

    class MetricRange(proto.Message):
        r"""A ``MetricRange`` is used when each window is good when the value x
        of a single ``TimeSeries`` satisfies ``range.min <= x < range.max``.
        The provided ``TimeSeries`` must have ``ValueType = INT64`` or
        ``ValueType = DOUBLE`` and ``MetricKind = GAUGE``.

        Attributes:
            time_series (str):
                A `monitoring
                filter <https://cloud.google.com/monitoring/api/v3/filters>`__
                specifying the ``TimeSeries`` to use for evaluating window
                quality.
            range_ (~.gm_service.Range):
                Range of values considered "good." For a one-
                ided range, set one bound to an infinite value.
        """

        time_series = proto.Field(proto.STRING, number=1)

        range_ = proto.Field(proto.MESSAGE, number=4, message=Range,)

    good_bad_metric_filter = proto.Field(
        proto.STRING, number=5, oneof="window_criterion"
    )

    good_total_ratio_threshold = proto.Field(
        proto.MESSAGE, number=2, oneof="window_criterion", message=PerformanceThreshold,
    )

    metric_mean_in_range = proto.Field(
        proto.MESSAGE, number=6, oneof="window_criterion", message=MetricRange,
    )

    metric_sum_in_range = proto.Field(
        proto.MESSAGE, number=7, oneof="window_criterion", message=MetricRange,
    )

    window_period = proto.Field(proto.MESSAGE, number=4, message=duration.Duration,)


__all__ = tuple(sorted(__protobuf__.manifest))
