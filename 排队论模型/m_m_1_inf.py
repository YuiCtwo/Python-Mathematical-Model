# -*- coding:utf-8 -*-
import math


# M/M/1/Infinite 模型
class MM1Infinite:

    def __init__(self, lambda_value, mu_value):
        self.arrive_per_time = lambda_value
        self.service_per_time = mu_value
        self.rho = self.arrive_per_time / self.service_per_time

    @property
    def available_probability(self):
        return 1 - self.rho

    @property
    def busy_probability(self):
        return self.rho

    def customer_probability(self, num):
        """计算恰有 num 个顾客的概率"""
        return self.rho ** num * (1 - self.rho)

    @property
    def aver_of_customer(self):
        """在店内的平均顾客数"""
        return self.rho / (1 - self.rho)

    @property
    def aver_of_wait_customer(self):
        """等待服务的平均顾客数"""
        return self.aver_of_wait_customer - self.rho

    @property
    def aver_of_staying(self):
        """每位顾客在店内的平均逗留时间"""
        return self.aver_of_customer / self.arrive_per_time

    def staying_probability(self, stay_time):
        """逗留超过 stay_time 的概率"""
        return math.e ** (-(self.service_per_time - self.arrive_per_time) * stay_time)

    @property
    def aver_wait_service(self):
        """每位顾客平均等待服务的时间"""
        return self.aver_of_wait_customer / self.arrive_per_time

