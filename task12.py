class Car:
#����������: ����� ��������: ����� (�����), ������, ��� �������,
#������, ����, ��� ���������, �������� ���������, ��� �����������, ���������, 
#������ �������, ��� �����
    def __init__(self, brand, model, age, millage, collor, en_type, en_pow,
                 transmission, cost, fuel_consuption, wheel):
        pass


class Engine:
#��������� - �������� ��������� ������ ����������
    def __init__(self, en_type, en_pow):
        self.en_type, self.en_pow = en_type, en_pow


    

class Transmission:
#����������� - �������� ��������� ������ ����������
    def __init__(self, tr_type, num_gear):
        pass


class Wheel:
#������ - �������� ������ ����������
#������, ������, ������ ��������, ��������
    def __init__(self, R, W, H, P):
        pass

    def pump_up():
        #�������� ������
        pass