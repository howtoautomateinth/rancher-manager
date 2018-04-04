import sys
from helper.yaml_reader import YamlReader
from services.rancher_factory import RancherFactory

def main(argv):
	yaml = YamlReader('./configuration/rancher_service.yaml')
	rancher_server_list = yaml.server_object

	rc_factory = RancherFactory(argv[0], rancher_server_list)
	rc = rc_factory.factory()
	rc.get_service_config()
	rc.get_request()

if __name__ == "__main__":
	main(sys.argv[1:])