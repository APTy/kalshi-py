from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.settlement_source import SettlementSource


T = TypeVar("T", bound="GetEventMetadataResponse")


@_attrs_define
class GetEventMetadataResponse:
    """
    Attributes:
        image_url (str): A path to an image that represents this event.
        settlement_sources (list['SettlementSource']): A list of settlement sources for this event.
        competition (Union[None, Unset, str]): Event competition.
        competition_scope (Union[None, Unset, str]): Event scope, based on the competition.
    """

    image_url: str
    settlement_sources: list["SettlementSource"]
    competition: Union[None, Unset, str] = UNSET
    competition_scope: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_url = self.image_url

        settlement_sources = []
        for settlement_sources_item_data in self.settlement_sources:
            settlement_sources_item = settlement_sources_item_data.to_dict()
            settlement_sources.append(settlement_sources_item)

        competition: Union[None, Unset, str]
        if isinstance(self.competition, Unset):
            competition = UNSET
        else:
            competition = self.competition

        competition_scope: Union[None, Unset, str]
        if isinstance(self.competition_scope, Unset):
            competition_scope = UNSET
        else:
            competition_scope = self.competition_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "image_url": image_url,
                "settlement_sources": settlement_sources,
            }
        )
        if competition is not UNSET:
            field_dict["competition"] = competition
        if competition_scope is not UNSET:
            field_dict["competition_scope"] = competition_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.settlement_source import SettlementSource

        d = dict(src_dict)
        image_url = d.pop("image_url")

        settlement_sources = []
        _settlement_sources = d.pop("settlement_sources")
        for settlement_sources_item_data in _settlement_sources:
            settlement_sources_item = SettlementSource.from_dict(settlement_sources_item_data)

            settlement_sources.append(settlement_sources_item)

        def _parse_competition(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        competition = _parse_competition(d.pop("competition", UNSET))

        def _parse_competition_scope(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        competition_scope = _parse_competition_scope(d.pop("competition_scope", UNSET))

        get_event_metadata_response = cls(
            image_url=image_url,
            settlement_sources=settlement_sources,
            competition=competition,
            competition_scope=competition_scope,
        )

        get_event_metadata_response.additional_properties = d
        return get_event_metadata_response

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
