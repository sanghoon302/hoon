##in_put file 양식 (반드시 txt 파일, 구분자는 공백) Name : list[0]
## Name OOO OOO OOO IP  Subnet  GateWay

from datetime import datetime

def calculate_network(ip_address, subnet_mask):
    # IP 주소와 서브넷 마스크를 '.'을 기준으로 분리하여 리스트로 변환
    ip_parts = ip_address.split('.')
    mask_parts = subnet_mask.split('.')

    # IP 주소와 서브넷 마스크의 각 부분을 정수로 변환
    ip = [int(part) for part in ip_parts]
    mask = [int(part) for part in mask_parts]

    # 네트워크 주소 계산
    network = [ip[i] & mask[i] for i in range(4)]

    # 브로드캐스트 주소 계산
    broadcast = [(ip[i] & mask[i]) | (255 ^ mask[i]) for i in range(4)]
    
    # 호스트 범위 계산
    host_min = network.copy()
    host_max = broadcast.copy()
    host_min[3] += 1
    host_max[3] -= 1

    # 계산 결과 반환
    return network, broadcast, host_min, host_max

file_path = 'IP.txt'

# IP 주소와 서브넷 마스크를 저장할 리스트 초기화
ip_addresses = []
subnet_masks = []
gateways = []


# 텍스트 파일 열기
with open(file_path, 'r') as file:
    # 파일에서 각 줄을 읽어옴
    lines = file.readlines()

    # 각 줄을 순회하면서 IP 주소와 서브넷 마스크, Gateway 주소를 공백으로 분리하여 리스트에 저장
    for line in lines:
        data = line.strip().split()
        Name = data[0]
        ip = data[4]
        subnet = data[5]
        gateway = data[6]
        ip_addresses.append(ip)
        subnet_masks.append(subnet)
        gateways.append(gateway)


# 계산 결과를 저장할 리스트 초기화
network_addresses = []
broadcast_addresses = []
host_mins = []
host_maxs = []

# IP 주소와 서브넷 마스크를 순회하면서 계산 결과 저장
for ip, subnet in zip(ip_addresses, subnet_masks):
    network, broadcast, host_min, host_max = calculate_network(ip, subnet)
    network_addresses.append(network)
    broadcast_addresses.append(broadcast)
    host_mins.append(host_min)
    host_maxs.append(host_max)




# 추출된 결과를 파일로 저장
output_file = "IP_Calculate_result" + datetime.today().strftime("%Y%m%d%H%M") + ".csv" # 저장할  파일명
# filt = "Name, IP, subnet, Network, broadcast, host"

with open(output_file, 'w', encoding='utf-8') as file:
    # output_file.write(filt + '\n')
    for i in range(len(ip_addresses)):
        broadcast_re = ".".join(str(part) for part in broadcast_addresses[i])
        network_re = ".".join(str(part) for part in network_addresses[i])
        host_min_re = ".".join(str(part) for part in host_mins[i])
        host_max_re = ".".join(str(part) for part in host_maxs[i])
        result = Name + "," + ip_addresses[i] + "," + subnet_masks[i] + "," + network_re + "," + broadcast_re + "," + host_min_re + "~" + host_max_re
        file.write(result + '\n')
