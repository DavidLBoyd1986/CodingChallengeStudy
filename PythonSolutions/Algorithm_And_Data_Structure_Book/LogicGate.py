class LogicGate:

    def __init__(self, n):
        self.name = n
        self.output = None

    def get_label(self):
        return self.name

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA is None:
            return int(input("Enter Pin A input for gate "+self.get_label()+"-->"))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        if self.pinB is None:
            return int(input("Enter Pin B input for gate "+self.get_label()+"-->"))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NAndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NOrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def perform_gate_logic(self):

        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 0 or b == 0:
            return 1
        else:
            return 0


class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def get_pin(self):
        if self.pin is None:
            return int(input("Enter Pin input for gate "+self.get_label()+"-->"))
        else:
            return self.pin.get_from().get_output()

    def set_next_pin(self,source):
        if self.pin is None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def perform_gate_logic(self):
        if self.get_pin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, init_from_gate, init_to_gate):
        self.from_gate = init_from_gate
        self.to_gate = init_to_gate

        init_to_gate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate


def main():
   # g1 = AndGate("G1")
   # g2 = AndGate("G2")
   # g3 = OrGate("G3")
   # g4 = NotGate("G4")
   # c1 = Connector(g1,g3)
   # c2 = Connector(g2,g3)
   # c3 = Connector(g3,g4)
   # print(g4.get_output())

    gate_one = AndGate("Gate One")
    gate_two = AndGate("Gate Two")
    combo_gate_one = NOrGate("Combo_Gate_One")
    connector_one = Connector(gate_one, combo_gate_one)
    connector_two = Connector(gate_two, combo_gate_one)
    print(combo_gate_one.get_output())

    gate_three = NAndGate("Gate Three")
    gate_four = NAndGate("Gate Four")
    combo_gate_two = AndGate("Combo_Gate_Two")
    connector_three = Connector(gate_three, combo_gate_two)
    connector_four = Connector(gate_four, combo_gate_two)
    print(combo_gate_two.get_output())

    print(combo_gate_one.get_output() == combo_gate_two.get_output())

main()