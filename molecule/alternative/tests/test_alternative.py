import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/etc/ipmi_exporter.yml",
    "/etc/systemd/system/ipmi_exporter.service",
    "/usr/local/bin/ipmi_exporter"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_service(host):
    s = host.service("ipmi_exporter")
    assert s.is_running
    # assert s.is_enabled


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9000")
    assert s.is_listening
