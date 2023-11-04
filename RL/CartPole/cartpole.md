## Triển khai một mô hình DDQN vào môi trường cartpole

### Giới thiệu về môi trường cartpole

- Gồm 1 thanh gỗ dựng đứng trên một tấm ván, ta phải di chuyển sao cho thanh gỗ được dựng đứng càng lâu càng tốt (không bị đổ)
- State là trạng thái của thanh gỗ, góc nghiêng của thanh gỗ
- Action: đẩy tấm ván sang trái hoặc sang phải
- Reward: Mỗi bước thời gian mà thanh gỗ được đứng vững, ta sẽ được một giá trị dương
- Policy: Định nghĩa cách agent quyết định hướng di chuyển của tấm ván nhằm giữ cho thanh gỗ ở trạng thái đứng lâu nhất

### Điều kiện để kết thúc 1 episode
(những điều kiện nhằm ngăn chặn episode kéo dài quá lâu, và giữ cho xe đẩy tập trung ở giữa màn hình mà không đi quá xa)
- Góc nghiêng của thanh ngang lớn hơn 12 độ hoặc 0.2095 radian.
- Vị trí của xe đẩy lớn hơn 2.4 đơn vị.
- Số bước trong một episode lớn hơn 500 cho phiên bản v1 của CartPole - và 200 cho phiên bản v0.

###  

- Tìm hiểu về cách cartpole hoạt động, các giá trị state, reward, .. của nó
  - [cartPoleExplained.py](https://github.com/AleksandarHaber/Demonstration-of-Cart-Pole-OpenAI-Gym-Reinforcement-Learning-Environment-in-Python-/blob/main/cartPoleExplained.py)


### Tham khảo:

- [Cart Pole - Gymnasium Documentation](https://gymnasium.farama.org/environments/classic_control/cart_pole/)
- 