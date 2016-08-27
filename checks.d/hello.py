from checks import AgentCheck
class HelloCheck(AgentCheck):
    def check(self, instance):
        self.gauge('ciao.world', 2)
