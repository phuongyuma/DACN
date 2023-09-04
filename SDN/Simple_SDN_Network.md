# Xây dựng một mạng SDN đơn giản với Ryu controller và Containernet

## SDN network

- Mạng SDN là kiến trúc mạng hiện đại và tiên tiến có khả năng tách biệt hoàn toàn giữa các phần mềm điều khiển (control plane) và phần cứng chuyển tiếp dữ liệu (data plane)

- Trong truyền thống, điều khiển và chuyển tiếp dữ liệu được tích hợp chặt chẽ trong các thiết bị mạng như switch và router. Điều này làm cho việc quản lý và điều khiển mạng phức tạp, đòi hỏi sự tương tác trực tiếp với từng thiết bị. Mạng SDN thay đổi cách tiếp cận này bằng cách tách biệt hai phần này.
  - Control Plane (Phần mềm điều khiển): Là trung tâm quản lý và quyết định cho toàn bộ mạng. Nó bao gồm các ứng dụng và phần mềm điều khiển, chịu trách nhiệm quản lý và theo dõi toàn bộ mạng. Phần mềm điều khiển tạo ra các chính sách (policy) và quyết định cách dữ liệu mạng phải được chuyển tiếp thông qua các thiết bị mạng.
  - Data Plane (Phần cứng chuyển tiếp dữ liệu): Là nơi thực hiện chuyển tiếp dữ liệu theo hướng dẫn từ phần mềm điều khiển. Phần cứng này có thể là các switch, router hoặc các thiết bị mạng khác. Chúng chỉ thực hiện việc chuyển tiếp dữ liệu mà không tham gia vào việc quyết định về cách xử lý dữ liệu.

![](IMG/2023-08-12-09-01-03.png)

- Giao thức OpenFlow: cho phép các ứng dụng trong phần mềm điều khiển gửi các yêu cầu và chỉ thị trực tiếp xuống phần cứng của chuyển tiếp dữ liệu

- Các lợi ích của mạng SDN:
  - Quản lý mạng nhanh chóng và linh hoạt hơn
  - Tích hợp dễ dàng với các ứng dụng và dịch vụ mạng
  - Tăng tính tin cậy và bảo mật của mạng
  - Tối ưu hóa việc sử dụng tài nguyên mạng

- Kiến trúc của SDN gồm 3 thành phần:
  - `SDN Networking Devices / Network Infrastructure`: Kiểm soát khả năng chuyển tiếp và xử lý dữ liệu cho mạng
  - `SDN Controller`: 
      - Nhận các hướng dẫn và yêu cầu từ tầng SDN Application và chuyển tiếp chúng đến các thành phần trong mạng.
      - Trích xuất thông tin về mạng từ các thiết bị phần cứng và liên lạc trở lại ứng dụng SDN với các số liệu thống kê và những gì đang xảy ra trong mạng
      - RYU, OpenDayLight, ONOS, FloodLight,..
    
  - `SDN Applications`: Là chương trình giao tiếp các hành vi và tài nguyên cần thiết thông qua APIs. Những ứng dụng này bao gồm quản lý mạng , phân tích, nghiên cứu,..
  
    ![](IMG/2023-08-12-13-13-52.png)


![](IMG/2023-08-12-13-10-44.png)


- Tham khảo thêm:
  - https://www.geeksforgeeks.org/software-defined-networking/
  - https://vietnix.vn/sdn-la-gi/
  - Udemy: Learn ​SDN, Mininet, Openflow, RYU Controller, Advanced Concepts( Master/Slave, Group table, Meter Table) Exercises - KNet Solutions

## Mininet

- Mininet có một công cụ mã nguồn mở với khả năng triển khai mô phỏng môi trường mạng ảo một cách nhanh chóng và dễ dàng. Được sử dụng phổ biến để mô phỏng các tình huống mạng phức tạp, kiểm tra giao thức mạng và phát triển ứng dụng SDN. Mininet có thể tạo mạng ảo trên một hoặc nhiều máy tính. Các tính năng của mininet:
  - Tạo ra mô hình mạng với các switch, host, link ảo
  - Topology mạng: Định nghĩa các kiến trúc mạng khác nhau như linear, tree, start (xác định cách các switch và hsot được kết nối với nhau)
    ![](IMG/2023-08-13-12-53-11.png)
  - Có thể thiết lập thông số như băng thông, độ trễ,...
  - Hỗ trợ các bộ controller khác nhau như Ryu, OpenDaylight, Floodlight (Có khả năng điều khiển và kiểm soát các switch mạng ảo)
  - Python API: có thể dùng python để lập trình sửa đổi và quản lý các kiến trúc mạng
  
- Ví dụ: `sudo mn --controller=remote,ip=127.0.0.1 --mac -i 10.1.1.0/24 --switch=ovsk,protocols=OpenFlow13 --topo=single,4`
  - Câu lệnh trên tạo ra một kiến trúc mạng với 4 switch theo topology linear, dùng giao thức OpenFlow13, switch ảo Open vSwitch

- Xóa ovs bridges và namespaces cũ: `sudo mn -c`
- Thực thi lệnh trên 1 host/node:
  - Dùng `xterm <host_name>` để mở một terminal xterm cho host
  - Thực hiện ngay trên mininet shell: `mininet> <host_name> command`

## OpenFlow 

- `OpenFlow Logical Switch`: là switch ảo hay switch logic được quản lý bởi bộ controller SDN thông qua giao thức OpenFlow, các thành phần của OFLS:
  - `Flow Table`: chứa các dòng (entries) của luồng dữ liệu mà controller gửi đến. Mỗi dòng bao gồm các trường để so khớp với dữ liệu gửi đến và các hành động cần thực hiện nếu dữ liệu khớp với một dòng cụ thể
    ![](IMG/2023-08-15-11-47-31.png)
  - `OpenFlow Controller`: Là phần quản lý mạng và điều khiển Logical Switch. Bản điều khiển là trí tuệ tập trung trong mô hình SDN, nơi quyết định về cách các luồng dữ liệu được xử lý và phân chia
  - `Ports`
  - `Flow Rules`: Các quy tắc xác định cách xử lý dữ liệu dựa trên các trường trong gói tin dữ liệu: địa chỉ Mac, địa chỉ IP, cổng nguồn, cổng đích,..
  - `Actions`: Mỗi dòng trong flow table đi kèm với một hay nhiều hành động. Các hành động này có thể bao gồm chuyển tiếp gói tin đến cổng cụ thể, gửi gói tin tới bản điều khiển để, thay đổi thông tin gói tin,..
  - `Match Fields`: Các trường trong gói tin dữ liệu được sử dụng để so khớp với các quy tắc trong flow table.
  - `Flow Statistics`: Thông tin về tình trạng và hiệu suất của các luồng dữ liệu trong logical switch: số lượng gói tin, băng thông, thời gian hoạt động
  - `Openflow Channel`: Kết nối OFLS với bộ controller, từ đó bộ controller có thể cấu hình và điều khiển switch, nhận các sự kiện từ switch và gửi các gói tin đi từ switch

![](IMG/2023-08-14-19-38-33.png)

- `OpenFlow Matching`
  ![](IMG/2023-08-15-11-49-06.png)

- `OpenFlow Messages`:
  - Controller to Switch:
    - Feature Request
    - Packet Out
    - Modify Flow Table
    - Modify Group Table
    - Modify Meter Table
    - OpenFlow Switch Description Request
    - OpenFlow Port Description Request
    - Openflow Statistics Request(Flow, Port, Flowtable, Aggregate, Group, Meter, Queue )
    - Role Request
    - Barrier Request
  - Asynchronous
    - Packet In
    - Flow Removed
  - Symmetric
    - Hello Message
    - Echo Message

- `Openflow Ports`
  - Physical ports: s1-eth1,..
  - Logical ports: vxlan0
  - Reserved ports: FLOOD, ALL, CONTROLLER, IN PORT, LOCAL, NORMAL

## Ryu controller 

- Ryu là một dự án mã nguồn mở cung cấp một framework cho việc phát triển các ứng dụng điều khiển mạng dựa trên giao thức OpenFlow. RYU cho phép bạn xây dựng các ứng dụng điều khiển mạng tùy chỉnh và linh hoạt, cho phép bạn tùy chỉnh hành vi của mạng theo cách bạn mong muốn.

- Kiểm tra port của Openflow: `netstat -ap | grep 6653`


- Run Ryu Applications: 
  - `ryu-manager ryu.app.<ryu application's name>`
  - `ryu-manager <python-file-name`
  - `ryu-manager <application1> <application2>`

- Flows:
  - Reactive Flows: Khi có gói tin mới xuất hiện thì switch sẽ gửi tới controller và controller sẽ gửi yêu cầu cấu hình luồng dữ liệu tới switch. Từ đó switch sẽ cấu hình bảng luồng với dữ liệu mới và xử lý tiếp các gói tin tương tự bằng luồng dữ liệu này.
  - Proacitve Flows: Cài đặt và cấu hình sẵn các luồng dữ liệu trên switch dựa trên các topology mạng và chính sách điều khiển

- Open vSwitch (OVS): Một switch ảo được sử dụng trong môi trường ảo hóa và SDN
  - Hiển thị danh sách các switch và bridge: `ovs-vsctl show`
  - Hiển thị các luồng dữ liệu trên switch
- Triển khai Ryu với Flow manager: `ryu-manager --observe-links ~/flowmanager.py ryu.app.simple_switch_13`

###

## Demo
### Demo 1

- Demo 1: Triển khai ryu và mininet trên cùng 1 máy
  - Dùng flowmanager làm giao diện quản lý
  - Dùng topology linear với 1 switch và 4 host
  
  ![](IMG/2023-08-14-18-33-30.png)

  ![](IMG/2023-08-14-18-31-39.png)

  ![](IMG/2023-08-14-18-32-41.png)

- Demo 2: Triển khai giống demo 1 nhưng dùng 6 switch và 6 host
  ![](IMG/2023-08-15-12-49-36.png)

- Demo 3: Triển khai giống demo 1 nhưng là với topology ring
  ![](IMG/2023-08-15-12-47-29.png)

- Demo 4: Triển khai các switch giống mô hình trong bài báo
  ![](IMG/2023-08-15-12-52-51.png)
  ![](IMG/2023-08-15-12-58-51.png)

  note: chưa ping được tới hết các node

### Demo 2 

- Mục tiêu:
  - Tìm hiểu về add flow cho các giao thức ngoài icmp
  - Tìm hiểu về rest api của ryu, gửi request add flow qua api

Rest API với Ryu: thêm ryu.app.ofctl_rest vào đuôi lệnh khi chạy Ryu
- Check stats qua api (done): curl -X GET http://localhost:8080/stats/switches
- Add flow đơn giản
- Xóa flow

-> Có thể add flow chung thay vì phải chỉnh theo từng giao thức icmp, tcp, udp (cần cập nhật thông tin arp ánh xạ cho mỗi hosts)

- Hoàn thành add flow cho 2 host 
- Chưa hoàn thành add flow cho tất cả host
- Chú ý tình trạng khi dùng vòng lặp để add flow, nên add table/group trước
- add_flow_2.py có thể ping được tới các host nhưng lại xuất hiện tình trạng các gói tin duplicate

