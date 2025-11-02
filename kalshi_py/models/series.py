from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.series_fee_type import SeriesFeeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.series_product_metadata_type_0 import SeriesProductMetadataType0
    from ..models.settlement_source import SettlementSource


T = TypeVar("T", bound="Series")


@_attrs_define
class Series:
    """
    Attributes:
        ticker (str): Ticker that identifies this series.
        frequency (str): Description of the frequency of the series. There is no fixed value set here, but will be
            something human-readable like weekly, daily, one-off.
        title (str): Title describing the series. For full context use you should use this field with the title field of
            the events belonging to this series.
        category (str): Category specifies the category which this series belongs to.
        tags (list[str]): Tags specifies the subjects that this series relates to, multiple series from different
            categories can have the same tags.
        settlement_sources (list['SettlementSource']): SettlementSources specifies the official sources used for the
            determination of markets within the series. Methodology is defined in the rulebook.
        contract_url (str): ContractUrl provides a direct link to the original filing of the contract which underlies
            the series.
        contract_terms_url (str): ContractTermsUrl is the URL to the current terms of the contract underlying the
            series.
        fee_type (SeriesFeeType): FeeType is a string representing the series' fee structure. Fee structures can be
            found at https://kalshi.com/docs/kalshi-fee-schedule.pdf. 'quadratic' is described by the General Trading Fees
            Table, 'quadratic_with_maker_fees' is described by the General Trading Fees Table with maker fees described in
            the Maker Fees section, 'flat' is described by the Specific Trading Fees Table.
        fee_multiplier (float): FeeMultiplier is a floating point multiplier applied to the fee calculations.
        additional_prohibitions (list[str]): AdditionalProhibitions is a list of additional trading prohibitions for
            this series.
        product_metadata (Union['SeriesProductMetadataType0', None, Unset]): Internal product metadata of the series.
    """

    ticker: str
    frequency: str
    title: str
    category: str
    tags: list[str]
    settlement_sources: list["SettlementSource"]
    contract_url: str
    contract_terms_url: str
    fee_type: SeriesFeeType
    fee_multiplier: float
    additional_prohibitions: list[str]
    product_metadata: Union["SeriesProductMetadataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.series_product_metadata_type_0 import SeriesProductMetadataType0

        ticker = self.ticker

        frequency = self.frequency

        title = self.title

        category = self.category

        tags = self.tags

        settlement_sources = []
        for settlement_sources_item_data in self.settlement_sources:
            settlement_sources_item = settlement_sources_item_data.to_dict()
            settlement_sources.append(settlement_sources_item)

        contract_url = self.contract_url

        contract_terms_url = self.contract_terms_url

        fee_type = self.fee_type.value

        fee_multiplier = self.fee_multiplier

        additional_prohibitions = self.additional_prohibitions

        product_metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.product_metadata, Unset):
            product_metadata = UNSET
        elif isinstance(self.product_metadata, SeriesProductMetadataType0):
            product_metadata = self.product_metadata.to_dict()
        else:
            product_metadata = self.product_metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "frequency": frequency,
                "title": title,
                "category": category,
                "tags": tags,
                "settlement_sources": settlement_sources,
                "contract_url": contract_url,
                "contract_terms_url": contract_terms_url,
                "fee_type": fee_type,
                "fee_multiplier": fee_multiplier,
                "additional_prohibitions": additional_prohibitions,
            }
        )
        if product_metadata is not UNSET:
            field_dict["product_metadata"] = product_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_product_metadata_type_0 import SeriesProductMetadataType0
        from ..models.settlement_source import SettlementSource

        d = dict(src_dict)
        ticker = d.pop("ticker")

        frequency = d.pop("frequency")

        title = d.pop("title")

        category = d.pop("category")

        tags = cast(list[str], d.pop("tags"))

        settlement_sources = []
        _settlement_sources = d.pop("settlement_sources")
        for settlement_sources_item_data in _settlement_sources:
            settlement_sources_item = SettlementSource.from_dict(settlement_sources_item_data)

            settlement_sources.append(settlement_sources_item)

        contract_url = d.pop("contract_url")

        contract_terms_url = d.pop("contract_terms_url")

        fee_type = SeriesFeeType(d.pop("fee_type"))

        fee_multiplier = d.pop("fee_multiplier")

        additional_prohibitions = cast(list[str], d.pop("additional_prohibitions"))

        def _parse_product_metadata(data: object) -> Union["SeriesProductMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_metadata_type_0 = SeriesProductMetadataType0.from_dict(data)

                return product_metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SeriesProductMetadataType0", None, Unset], data)

        product_metadata = _parse_product_metadata(d.pop("product_metadata", UNSET))

        series = cls(
            ticker=ticker,
            frequency=frequency,
            title=title,
            category=category,
            tags=tags,
            settlement_sources=settlement_sources,
            contract_url=contract_url,
            contract_terms_url=contract_terms_url,
            fee_type=fee_type,
            fee_multiplier=fee_multiplier,
            additional_prohibitions=additional_prohibitions,
            product_metadata=product_metadata,
        )

        series.additional_properties = d
        return series

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
