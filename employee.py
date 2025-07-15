# Chris Smith
# Chapter 15 - Lab 1
# 07/14/2025

from dataclasses import dataclass

# Employee base class
@dataclass
class Employee:
    name: str
    hours_worked: float
    hourly_rate: float

    def calc_pay(self):
        return self.hours_worked * self.hourly_rate

# Salesperson subclass with commission logic
@dataclass
class Salesperson(Employee):
    weekly_sales: float
    commission_rate: float

    def calc_pay(self):
        base = super().calc_pay()
        commission = self.weekly_sales * self.commission_rate
        return base + commission
