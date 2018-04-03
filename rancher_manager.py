import sys
from helper.yaml_reader import YamlReader
from services.rancher_factory import RancherFactory

def main(argv):
	yaml = YamlReader('hello world')
	rc_factory = RancherFactory(argv[0])
	rc = rc_factory.factory()
	rc.get_service_config()
	rc.get_request()

if __name__ == "__main__":
	main(sys.argv[1:])