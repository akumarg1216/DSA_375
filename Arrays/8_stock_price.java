public class stock_price {
    
    static int maxProfit(int[] prices){
        int globalProfit = 0;
        int minBuyPrice = Integer.MAX_VALUE;

        for(int i=0; i<prices.length; i++){
            if(minBuyPrice > prices[i]){
                minBuyPrice = prices[i];
            }

            int currentProfit = prices[i] - minBuyPrice;

            if(currentProfit > globalProfit){
                globalProfit = currentProfit;
            }
        }
        return globalProfit;
    }

    public static void main(String[] args) {
        int[] prices = {7,6,4,3,1};
        System.out.println(maxProfit(prices));        
    }
}


