# DACN
 
## Note of meeting and task

### 18/7/2023

- Bắt đầu được giao bài báo để đọc và tìm hiểu

### 1/8/2023

- Đã đọc nhưng chưa dịch hết bài báo, chỉ dịch được tầm 40%
- Tìm hiểu các khái niệm/ công nghệ xuất hiện trong bài báo như: SDN network, traffic analyzer, deep packet inspection, IDPS,  deep deterministic policy gradient, deep reinforcement learning (chưa nắm rõ được)
- Được giao xây dựng một mạng SDN đơn giản với mininet/containernet và Ryu controller/OpenDaylight  

### 22/8/2023

- Tìm hiểu về SDN, Ryu Controller, Mininet, Containernet, OpenFlow (Chưa nắm rõ về Ryu Controller cho lắm)
- Triển khai mạng SDN đơn giản với Ryu Controller và Mininet
  - Dùng flow-manager để làm giao diện quản lý
  - Hiểu được cách dùng mininet để tạo các host và switch
  - Hiểu được cách kiểm tra kết nối ICMP, TCP, UDP cho mininet
  - Triển khai được topology linear gồm 4 switch, mỗi switch chứa 1 host (các host có thể ping được tới nhau)
  - Triển khai topology ring gồm 4 switch, mỗi switch chứa 1 host (các host có thể ping tới nhau nhưng chưa kết nối được udp, tcp)
- Được giao:
  - Tìm hiểu về add flow cho các giao thức ngoài icmp
  - Tìm hiểu về rest api của ryu, gửi request add flow qua api

### 5/9/2023

- Hiểu và tiến hành dùng RYU OFCTL REST API:
  - OFCTL - Openflow control using REST Interface
  - Ứng dụng ryu.app.ofctl_rest có sẵn của RYU cung cấp REST API cho ta để có thể cấu hình, cập nhật các giá trị và luồng của switch (https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html)

- Hiểu và tiến hành add flow cho switch:
  - Dùng lệnh curl để add flow
  - Dùng flow-manager để add flow
  - Dùng thư viện request của python để add nhiều flow 1 lúc 
    - [Ví dụ](SDN\add_flow.py)

- Khi add flow, ta không thêm giá trị ip_proto thì RYU sẽ nhận định là match với tất cả giao thức
- Tiến độ triển khai: 
  - Add flow cho topology linear thành công, các host có thể ping được với nhau
  - Đối với topology ring gồm 5 switch, mỗi switch gồm 1 host
    - Add flow cho 1 host ping được với 1 host khác, nhưng khi add flow cho tất cả host như vậy thì lại không host nào ping được tới nhau
    - Với [add_flow_2.py](SDN\add_flow_2.py) thì ban đầu khi ping thì xuất hiện tình trạng Duplicate, sau đó thì các host không ping được tới nhau (có lúc được có lúc không)

## 9/9/2023

- Vẫn còn mắc kẹt ở việc add flow cho vòng lặp:
  - Tạo 1 mạng SDN kết nối với RYU gồm 3 switch, mỗi switch có 1 host, 3 switch nối với nhau tạo thành topo ring
    - Cả 3 switch đều ping được tới nhau
    - Host h1 và host h2 ping được tới nhau, nhưng host h3 không thể ping đi hay ping tới từ các host khác 
  ==>> sau khi thêm bảng arp thì thành công các host ping được tới nhau???? chưa hiểu lý do lắm

## 13/9/2023

- Đã triển khai được mô hình giống như bài báo:
  - Đã test với protocol http, icmp, udp, tcp
  - Xuất hiện tình trạng có những gói tin được gửi đi liên tục => cấu hình vẫn có vấn đề

- Hướng tìm hiểu tiếp tục:
  - Viết một đoạn code làm gọn lại phần add flow
  - Thay vì add flow thì xây dựng 1 RYU application để thực hiện add flow ngắn gọn và nhanh chóng hơn
  - Tìm lỗi sai của cấu hình và sửa lại
  - Tìm hiểu làm thế nào để triển khai Deep Reinforcement Learning trên RYU và mạng SDN được xây

- Task được giao:
  - Đọc bài báo và tìm trong bài báo các giá trị state, action, reward, policy theo RL
  - Tìm hiểu về Qlearning và lấy code game về sửa

## 25/9/2023

- Đọc hiểu code, hiểu cách RL chạy qua debug
- Tạo các tham số giống bài báo rồi cho thay vào code của cartpole để chạy

## 9/10/2023

- Một vài vấn đề mắc phải:
  - Đã triển khai được DQN sau khi tham khảo trên mạng nhưng vẫn còn các vấn đề sau:
    - Khi record video thì chưa tạo được video cartpole chạy thành công (Có thể do lúc train lỗi hoặc chưa train được lâu như tác giả)
  - Chưa tạo được env cho mạng


- Xem thử output của action là ma trận 1 chiều hay nhiều chiều
- Xem thử input của State có phải là ma trận nhiều chiều không
- Xác định trước state và action theo bảng trong paper rồi tiến hành triển khai DQN
- Triển DDQN thành DQN trong code cartpole


- Input
  - State 
    - State là ma trận 2 chiều: // chưa chắc lắm vì khác với công thức của bài báo nhưng lại đúng vài table exmaple của bài báo
      - Mỗi cột chứa 2 giá trị:
        - Trạng thái tài nguyên được lấy mẫu pj 
        - Trạng thái của bộ phân tích lưu lượng được trọng dk
      - Mỗi cột có m hàng (m là số điểm lấy mẫu)

- Hàm SelectAction:
  - input là state và index của episode hiện tại
  - Khác biệt giữa việc chọn hành động của bài báo và của cartpole
    - Cartpole cần chọn 1 hành động từ 2 hành động
    - Bài báo cần chọn 3 hành động từ 3 dãy hành động khác nhau
      - determines the sampling points pj ∈ O
      - determines which traffic analyzer to assign at each sampling point
      - determines the reduction of the sampling rate


### 30/10/2023

- Tìm hiểu thuật toán DDPG: tìm code, giả lập dữ liệu
- Tìm hiểu về A2C,PPO,actor-critic
- Báo cáo tiếp vào ngày 13/11/2023, note lại các công việc cần làm để hoàn thành đồ án, đánh dấu những công việc đã hoàn thành, nếu chưa hoàn thành được 5/x thì phải nhanh chóng hơn

### 27/11/2023

- Xem coi action, reward có phụ thuộc vào next state không
- Hoàn tất xây dựng mô hình theo figure 3 của bài báo

### 11/12/2023

- Đã thêm các phần relay buffer, update actor model, critic model
- Gặp trục trặc với phần soft update
- Ràng buộc state để tránh các state vô nghĩa
- tính toán reward

### 25/12/2023

- Trục trặc:
  - Time step and sampling period
  - Chưa rõ cách tính total flow và sampled flow
  - Chưa rõ về Steering Overhead Penalty rv (điểm rv sẽ được trừ vào reward nếu chi phí điều hướng tới từ sampled points tới traffic analyzers quá cao)
  - Các thông số như hiệu suất, khả năng tính toán, xử lý của bộ phân tích lưu lượng, tổng số luồng,.. đang được tạo giả

### 8/1/2024

- Chưa tạo được traffic analyzer trong mininet
- Sửa lại phần sampling period
- Sửa lại topology trong mininet cho mượt hơn.
- Các host trong mininet liên tục gửi gói tin và chưa dừng lại

- Tạo traffic analyzer external, và thử ping từ trong mininet ra host ở ngoài
- Vai trò của traffic analyzer trong mô hình
## List to do

- [X] Đọc và tìm hiểu về đề tài và mô hình cần triển khai
- [X] Tìm hiểu và triển khai mạng SDN
  - [X] Tìm hiểu về SDN, Ryu Controller, Mininet, Containernet, OpenFlow (Chưa nắm rõ về Ryu Controller cho lắm)
  - [X] Triển khai mạng SDN đơn giản với Ryu Controller và Mininet
  - [X] Triển khai mạng SDN gồm 6 Switch giống mô hình và các máy kết nối với các Switch có thể ping tới nhau 
- [X] Tìm hiểu và triển khai thuật toán DDQN (ngoài lề)
  - [X] Triển khai DDQN với cartpole
  - [ ] Triển khai DDQN theo mô hình
- [ ] Tìm hiểu và triển khai thuật toán DDPG
  - [X] Triển khai Policy Gradient với cartpole
  - [X] Tìm hiểu về A2C, PPO, actor-critic
  - [X] Triển khai A2C với cartpole
  - [ ] Triển khai DDPG với cartpole
  - [ ] Triển khai DPG, actor-critic với mô hình giống như bài báo
    - [ ] Xây dựng class NetworkEnv (môi trường cho bài báo)
      - [ ] Tạo State Space, Action Space (use random to fake input for model)
      - [ ] Hàm reset() 
      - [ ] Hàm step() 
      
  - [ ] Triển khai DDPG với mô hình giống như trong bài báo
- [ ] Triển khai thuật toán DDPG với mạng SDN
  - [ ] Triển khai agent với DDPG để nhận input từ mạng SDN đã triển khai
  - [ ] Triển khai và huấn luyện agent với DDPG theo mô hình được giao
- [ ] Viết báo cáo 

