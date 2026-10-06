from finance_tracker.reports import get_category_breakdown


def test_category_breakdown():
    expenses = [
        {
            "date": "2026-10-06",
            "amount": 500,
            "category": "Food",
            "description": "Lunch"
        },
        {
            "date": "2026-10-06",
            "amount": 300,
            "category": "Transport",
            "description": "Bus"
        },
        {
            "date": "2026-10-06",
            "amount": 200,
            "category": "Food",
            "description": "Snacks"
        }
    ]

    result = get_category_breakdown(expenses)

    assert result["Food"] == 700
    assert result["Transport"] == 300
