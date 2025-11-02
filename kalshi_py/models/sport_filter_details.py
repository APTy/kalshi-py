from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sport_filter_details_competitions import SportFilterDetailsCompetitions


T = TypeVar("T", bound="SportFilterDetails")


@_attrs_define
class SportFilterDetails:
    """
    Attributes:
        scopes (list[str]): List of scopes available for this sport
        competitions (SportFilterDetailsCompetitions): Mapping of competitions to their scope lists
    """

    scopes: list[str]
    competitions: "SportFilterDetailsCompetitions"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scopes = self.scopes

        competitions = self.competitions.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scopes": scopes,
                "competitions": competitions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sport_filter_details_competitions import SportFilterDetailsCompetitions

        d = dict(src_dict)
        scopes = cast(list[str], d.pop("scopes"))

        competitions = SportFilterDetailsCompetitions.from_dict(d.pop("competitions"))

        sport_filter_details = cls(
            scopes=scopes,
            competitions=competitions,
        )

        sport_filter_details.additional_properties = d
        return sport_filter_details

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
