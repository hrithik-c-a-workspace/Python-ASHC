import psutil

class SystemMonitor:

    def __init__(self):
        data = self.refresh_data()

        self.ram_data = data['ram']
        self.cpu_data = data['cpu']
        self.disk_data = data['disk']

    def refresh_data(self):
        return {
            'ram': psutil.virtual_memory()._asdict(),
            'cpu': {
                'count': psutil.cpu_count(),
                'frequency': psutil.cpu_freq()._asdict(),
                'percent': psutil.cpu_times_percent()._asdict()
            },
            'disk':  psutil.disk_usage('/')._asdict()  
        }

    def getRamInfo(self):
        return { 
            'total': self.convert_bytes(self.ram_data['total']),
            'available': self.convert_bytes(self.ram_data['available']),
            'percent': self.ram_data['percent'],
            'used': self.convert_bytes(self.ram_data['used'])     
        }
    
    def getCpuInfo(self):
        return {
            'count': self.cpu_data['count'],
            'frequency': self.cpu_data['frequency'],
        }
    
    def getDiskInfo(self):
        return {
            'total': self.convert_bytes(self.disk_data['total']),
            'used': self.convert_bytes(self.disk_data['used']),
            'free': self.convert_bytes(self.disk_data['free']),
            'percent': self.disk_data['percent']
        }


    @staticmethod
    def convert_bytes(size_in_bytes):
        return round(size_in_bytes / (1024**3), 2)

    def display_ram_info(self):
        info = self.getRamInfo()
        print(f"RAM Used: {info['percent']}%, Total: {info['total']}GB, Available: {info['available']}GB, Used: {info['used']}GB")

    def display_cpu_info(self):
        info = self.getCpuInfo()
        print(f"CPU Frequency: {info['frequency']['current']}, Total CPU Cores: {info['count']}")

    def display_disk_info(self):
        info = self.getDiskInfo()
        print(f"Disk Used: {info['percent']}%, Total: {info['total']}GB, Free: {info['free']}GB, Used: {info['used']}GB")    

        

monitor = SystemMonitor()
monitor.display_ram_info()
monitor.display_cpu_info()
monitor.display_disk_info()
