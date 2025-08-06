from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_multivariate_event_collection import (
        GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection,
    )


T = TypeVar("T", bound="GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionResponse")


@_attrs_define
class GithubComKalshiExchangeInfraSvcApi2ModelGetMultivariateEventCollectionResponse:
    """
    Attributes:
        multivariate_contract (Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection]):
    """

    multivariate_contract: Union[Unset, "GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        multivariate_contract: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.multivariate_contract, Unset):
            multivariate_contract = self.multivariate_contract.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if multivariate_contract is not UNSET:
            field_dict["multivariate_contract"] = multivariate_contract

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.github_com_kalshi_exchange_infra_svc_api_2_model_multivariate_event_collection import (
            GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection,
        )

        d = dict(src_dict)
        _multivariate_contract = d.pop("multivariate_contract", UNSET)
        multivariate_contract: Union[Unset, GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection]
        if isinstance(_multivariate_contract, Unset):
            multivariate_contract = UNSET
        else:
            multivariate_contract = GithubComKalshiExchangeInfraSvcApi2ModelMultivariateEventCollection.from_dict(
                _multivariate_contract
            )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_response = cls(
            multivariate_contract=multivariate_contract,
        )

        github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_response.additional_properties = d
        return github_com_kalshi_exchange_infra_svc_api_2_model_get_multivariate_event_collection_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
