class Instance:
    instance = None

    def __init__(self, instance):
        self.instance = instance

    def get_ip(self):
        return self.instance.public_ip_address

    def get_state(self):
        return self.instance.state

    def reload(self):
        self.instance.reload()

    def stop(self):
        self.instance.stop()

    def terminate(self):
        self.instance.terminate()

    def wait_until_running(self):
        self.instance.wait_until_running()

    def wait_until_stopped(self):
        self.instance.wait_until_stopped()

    def wait_until_terminated(self):
        self.instance.wait_until_terminated()
