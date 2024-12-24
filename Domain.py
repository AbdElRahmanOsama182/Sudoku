class Domain:

    def __init__(self, domain=0b111111111):
        self.domain = domain

    def have(self, number):
        return self.domain & (1 << (number - 1))
        
    def remove(self, number):
        if not self.have(number):
            return False
        self.domain &= ~(1 << (number - 1))
        return True

    def add(self, number):
        if self.have(number):
            return False
        self.domain |= (1 << (number - 1))
        return True

    def is_empty(self):
        return self.domain == 0

    def is_singleton(self):
        return self.domain & (self.domain - 1) == 0 and self.domain != 0

    def get_value(self):
        if self.is_singleton():
            return self.domain.bit_length()
        return 0
    
    def get_domain(self):
        return [i + 1 for i in range(9) if self.domain & (1 << i)]

    def domain_size(self):
        return bin(self.domain).count('1')

    def __str__(self):
        return str(self.get_domain())
    
    def copy(self):
        return Domain(self.domain)

if __name__ == '__main__':
    domain = Domain(0b000000001)
    print(domain)
    domain.remove(1)
    print(domain)
    # domain.add(3)
    print(domain)
    print(domain.is_empty())
    print(domain.is_singleton())
    print(domain.get_value())
    print(domain.get_domain())

