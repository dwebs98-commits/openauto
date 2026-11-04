"""Core auction bid and profit calculations for OpenAuto."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Deal:
    resale: float = 9500
    auction_fees: float = 850
    repairs: float = 500
    transportation: float = 250
    other_costs: float = 300
    target_profit: float = 1500

    def __post_init__(self):
        if any(value < 0 for value in vars(self).values()):
            raise ValueError("All amounts must be nonnegative")

    @property
    def costs_excluding_bid(self) -> float:
        return self.auction_fees + self.repairs + self.transportation + self.other_costs

    @property
    def max_bid(self) -> float:
        return self.resale - self.costs_excluding_bid - self.target_profit

    def profit_at_bid(self, bid: float) -> float:
        if bid < 0:
            raise ValueError("Bid must be nonnegative")
        return self.resale - bid - self.costs_excluding_bid

    def roi_at_bid(self, bid: float) -> float:
        investment = bid + self.costs_excluding_bid
        return self.profit_at_bid(bid) / investment if investment > 0 else 0.0
