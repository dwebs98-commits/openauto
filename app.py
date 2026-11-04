"""OpenAuto v0.1: local-first vehicle auction deal analyzer."""
import csv
import io
import streamlit as st
from calculator import Deal

st.set_page_config(page_title="OpenAuto", page_icon="🚗", layout="wide")
st.title("🚗 OpenAuto")
st.caption("Open-source auction flip analyzer · v0.1 · Estimates are not appraisals")

with st.sidebar:
    st.header("Vehicle details")
    year = st.number_input("Year", 1980, 2035, 2018, step=1)
    make = st.text_input("Make", "Hyundai")
    model = st.text_input("Model", "Ioniq Hybrid")
    mileage = st.number_input("Mileage", min_value=0, value=46432, step=1000)
    title_status = st.selectbox("Title status", ["Clean", "Salvage", "Rebuilt", "Bill of Sale", "Unknown"])
    vehicle_url = st.text_input("Auction listing URL (optional)")

st.subheader("Deal assumptions")
a, b = st.columns(2)
with a:
    resale = st.number_input("Expected resale price ($)", min_value=0.0, value=9500.0, step=100.0)
    fees = st.number_input("Auction and buyer fees ($)", min_value=0.0, value=850.0, step=50.0)
    repairs = st.number_input("Repairs and reconditioning ($)", min_value=0.0, value=500.0, step=50.0)
with b:
    transport = st.number_input("Transportation ($)", min_value=0.0, value=250.0, step=50.0)
    other = st.number_input("Other costs ($)", min_value=0.0, value=300.0, step=50.0)
    target = st.number_input("Target profit ($)", min_value=0.0, value=1500.0, step=100.0)

deal = Deal(resale, fees, repairs, transport, other, target)
max_bid = deal.max_bid
st.divider()
metric_a, metric_b, metric_c = st.columns(3)
metric_a.metric("Maximum hammer bid", f"${max_bid:,.0f}" if max_bid >= 0 else "No viable bid")
metric_b.metric("Costs excluding bid", f"${deal.costs_excluding_bid:,.0f}")
metric_c.metric("Target profit", f"${target:,.0f}")

current_bid = st.number_input("Proposed/current hammer bid ($)", min_value=0.0, value=4900.0, step=100.0)
profit = deal.profit_at_bid(current_bid)
roi = deal.roi_at_bid(current_bid)
st.metric("Estimated profit at proposed bid", f"${profit:,.0f}")
st.metric("Estimated return on total invested cash", f"{roi:.1%}")
if max_bid < 0:
    st.error("Your costs and target profit exceed expected resale value. Pass on this deal under these assumptions.")
elif current_bid <= max_bid:
    st.success(f"Within target: ${max_bid-current_bid:,.0f} of bidding room remains.")
else:
    st.warning(f"Above your target maximum by ${current_bid-max_bid:,.0f}. Consider passing.")

st.subheader("Repair uncertainty")
extra_repairs = st.slider("Additional unexpected repair cost ($)", 0, 3000, 500, 100)
st.write(f"Profit if repairs run ${extra_repairs:,} over budget: **${profit-extra_repairs:,.0f}**")

st.subheader("Watchlist")
st.caption("Stored in this browser session only; download CSV to keep your records.")
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []
if st.button("Add scenario to watchlist"):
    st.session_state.watchlist.append({
        "year": year, "make": make, "model": model, "mileage": mileage,
        "title_status": title_status, "auction_url": vehicle_url,
        "resale": resale, "auction_fees": fees, "repairs": repairs,
        "transportation": transport, "other_costs": other,
        "target_profit": target, "max_bid": max_bid,
        "proposed_bid": current_bid, "estimated_profit": profit,
    })
if st.session_state.watchlist:
    st.dataframe(st.session_state.watchlist, use_container_width=True)
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=list(st.session_state.watchlist[0]))
    writer.writeheader()
    writer.writerows(st.session_state.watchlist)
    st.download_button("Download watchlist CSV", output.getvalue(), "openauto_watchlist.csv", "text/csv")
    if st.button("Clear watchlist"):
        st.session_state.watchlist = []
        st.rerun()

st.info("Verify actual auction fees, title eligibility, taxes, repairs, resale comps, and applicable dealer rules before bidding. This tool does not access auction listings automatically.")
