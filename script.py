import psutil

class SystemMonitor:

    def getRamInfo(self):
        ram_info = psutil.virtual_memory()._asdict()
        
        return { 
            'total': self.convert_bytes(ram_info['total']),
             'available': self.convert_bytes(ram_info['available']),
             'percent': self.convert_bytes(ram_info['percent']),
             'used': self.convert_bytes(ram_info['used'])     
            }


    @staticmethod
    def convert_bytes(size_in_bytes):
        return round(size_in_bytes / (1024**3), 2)

    def display_ram_info(self):
        info = self.getRamInfo()
        print(f"Total RAM: {info['total']}GB, Available RAM: {info['available']}GB, Used RAM: {info['used']}GB")
        

monitor = SystemMonitor()
monitor.display_ram_info()
