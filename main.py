from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Buyer Intel API", version="1.0.0")


class BuyerProfile(BaseModel):
    id: int
    name: str
    company: str
    industry: str
    revenue_range: str
    location: str


BUYERS: list[BuyerProfile] = [
    BuyerProfile(
        id=1,
        name="Alex Rivera",
        company="Northwind Logistics",
        industry="Supply chain",
        revenue_range="$10M–$50M",
        location="Chicago, IL",
    ),
    BuyerProfile(
        id=2,
        name="Jordan Lee",
        company="Brightline Health",
        industry="Healthcare technology",
        revenue_range="$50M–$100M",
        location="Boston, MA",
    ),
    BuyerProfile(
        id=3,
        name="Sam Patel",
        company="GreenLeaf Foods",
        industry="Consumer packaged goods",
        revenue_range="$100M–$250M",
        location="Austin, TX",
    ),
    BuyerProfile(
        id=4,
        name="Taylor Morgan",
        company="Atlas Manufacturing",
        industry="Industrial equipment",
        revenue_range="$250M–$500M",
        location="Detroit, MI",
    ),
    BuyerProfile(
        id=5,
        name="Riley Chen",
        company="Summit Financial Partners",
        industry="Financial services",
        revenue_range="$500M+",
        location="New York, NY",
    ),
]


@app.get("/buyers", response_model=list[BuyerProfile])
def list_buyers() -> list[BuyerProfile]:
    return BUYERS


@app.get("/buyers/{buyer_id}", response_model=BuyerProfile)
def get_buyer(buyer_id: int) -> BuyerProfile:
    for buyer in BUYERS:
        if buyer.id == buyer_id:
            return buyer
    raise HTTPException(status_code=404, detail="Buyer not found")
