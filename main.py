from trade_platform.src.agent.tcn_agent import tcn_agent
from trade_platform.src.agent.simple_agent import simple_agent
from trade_platform.src.agent.agent_thread import agent_thread
from trade_platform.src.trade_platform.trade_platform import trade_platform
from tcn_modeling import tcn
import matplotlib.pyplot as plt

if __name__ == "__main__":
    #t = trade_platform(length=5000, data_path=r'data\US1.ATVI_200505_200507.txt', enable_plot=False,random=False, type = "minute")
    # when inport csv or other data file, be sure to remove the headers.

    # trained_agent = tcn_agent(trainset = 0, arima = False, model='1', moments=17)#, loadModel = 'model1custom.h5'
    # # trained_agent.train('data/US1.ABT_small_training.txt')
    # t.add_agent(trained_agent)
    # t.start()
    models = {r'model_3+moments_30+batch_sizeNone.h5': 30,
              r'model_3+moments_45+batch_sizeNone.h5': 45}
    for moments in [15,30,45]:
        Tcn = tcn(model = 3, data_path=r'data\US1.ABT_190504_200519.txt', moments = moments);
        Tcn.train()

        Tcn.test_set(data_path = r'data\US1.ABT_test.txt')
        #tcn.test()
        predict, actual = Tcn.predict()

        #graphs predicted percentage change over 100 minutes
        for j in [100,500,1000]:
            predict1 = 10** predict[:j]
            actual1 = 10** actual[:j]
            for i in range(len(predict1) - 1):
                        predict1[i+1] = predict1[i+1] * predict1[i]
                        actual1[i+1] = actual1[i+1] * actual1[i]

            plt.plot(predict1, c = "blue", label = "predicted")
            plt.plot(actual1, c = "red", label = "actual")

                    # fname = f'moments_{moments}+{i}minute_predict-vs-actual'
                    # plt.savefig(fname)
            plt.show()
            plt.clf()




# If you want to use your own mrkt_data format:
# check CS175-Trade-Platform/src/util/mrkt_data.py first
# for example, the order of your CSV is different from mrkt_data
# first define a function
def mrkt_data_example(self, args,time = 0 ):
    self.price = args[0]
    self.spacial_data1 = args[1]
    self.spacial_data2 = args[2]
    # ......
    self.time  = time # time here is only as a reference. Use with discretion
# pass this function to cos_mrkt_data parameter of trade_platform
# example = trade_platform(length=5000, data_path='[PATH HERE]', enable_plot=False,random=False,cos_mrkt_data= mrkt_data_example)

'''/*
 * Synchronous(default) / Asynchronous(deprecated)
 * Market / Agent
 *
 * Trade platform
 *
*/'''
