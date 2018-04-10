import sys
from helper.yaml_reader import YamlReader
from helper.yaml_generator import YamlGenerator
from services.rancher_factory import RancherFactory

def main(argv):
	yaml = YamlReader('./configuration/rancher_service_to_update.yaml')
	rancher_server_list = yaml.server_object

	rc_factory = RancherFactory(argv[0], rancher_server_list)
	rc = rc_factory.factory()
	rc.upgrade()

	yaml_generator = YamlGenerator('./configuration/rancher_list_to_yaml.yaml')
	yaml_generator.gathering()
	yaml_generator.generate()

if __name__ == "__main__":
	main(sys.argv[1:])