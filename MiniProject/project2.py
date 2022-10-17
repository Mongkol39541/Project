from proj_data import Datanumber
class acx:
    def main(num):
        p_number = num
        sum_1 = 0
        sum_2 = 0
        double_num = []
        number = p_number
        for i in number:
            sum_1 += int(i)
        data = Datanumber.number_phone()
        mean_num = data[str(sum_1)]
        for k in range(len(p_number) - 2):
            duo1 = p_number[k + 1]
            duo2 = duo1 + p_number[k + 2]
            double_num.append(duo2)
        for j in double_num:
            sum_2 += (Datanumber.percent_number()[j])
        sum_2 //= (len(double_num) / 100)
        percent_num = (int(sum_2))
        return mean_num, percent_num, 100 - percent_num