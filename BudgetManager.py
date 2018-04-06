class BudgetManager:
    @classmethod
    def account_budget(cls, period):
        effective_amount = 0
        for budget in cls.budgets:
            if period and cls.is_in_budget_time(period, budget):
                effective_amount += period.effective_days(budget) * budget.amount_of_day()
        return effective_amount

    @classmethod
    def get_budgets(cls, *budgets):
        cls.budgets = budgets

    @classmethod
    def is_in_budget_time(cls, period, budget):
        return period.end_time > budget.first_day() and period.start_time < budget.last_day()


