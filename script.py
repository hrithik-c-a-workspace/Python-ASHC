import psutil

class SystemMonitor:

    def __init__(self):
        self.data = self.refresh_data()

    def refresh_data(self):
        return psutil.virtual_memory()._asdict()

    def getRamInfo(self):
        return { 
             'total': self.convert_bytes(self.data['total']),
             'available': self.convert_bytes(self.data['available']),
             'percent': self.data['percent'],
             'used': self.convert_bytes(self.data['used'])     
            }


    @staticmethod
    def convert_bytes(size_in_bytes):
        return round(size_in_bytes / (1024**3), 2)

    def display_ram_info(self):
        info = self.getRamInfo()
        print(f"RAM Used: {info['percent']}%, Total: {info['total']}GB, Available: {info['available']}GB, Used: {info['used']}GB")
        

monitor = SystemMonitor()
monitor.display_ram_info()
