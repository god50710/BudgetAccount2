from datetime import datetime
from unittest import TestCase
from Budget import Budget
from BudgetManager import BudgetManager
from Period import Period


class TestBudgetManager(TestCase):
    def test_no_period(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(None), 0)

    def test_20_days_period_in_budget_time(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 3, 1), datetime(2017, 3, 20))), 20)

    def test_period_before_budget_time(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 2, 27),datetime(2017, 2, 28))), 0)

    def test_period_after_budget_time(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 4, 1),datetime(2017, 4, 3))), 0)

    def test_period_overlapping_budget_first_day(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 2, 27),datetime(2017, 3, 3))), 3)

    def test_period_overlapping_budget_last_day(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 3, 27),datetime(2017, 4, 2))), 5)

    def test_invalid_period(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 31))
        self.assertRaises(Exception, Period, datetime(2017, 3, 27), datetime(2017, 3, 21))

    def test_amount_is_100_per_day(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 3100))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 3, 20), datetime(2017, 3, 26))), 700)

    def test_multiple_budgets_with_overlapping_period(self):
        bm = BudgetManager
        bm.get_budgets(Budget("201703", 3100), Budget("201704", 120))
        self.assertEqual(bm.account_budget(Period(datetime(2017, 3, 30), datetime(2017, 4, 3))), 212)
