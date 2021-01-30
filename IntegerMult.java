public class IntegerMult{
    public static void main(String args[]){
        String x = "3141592653589793238462643383279502884197169399375105820974944592";
        String y = "2718281828459045235360287471352662497757247093699959574966967627";
        String r = int_multi(x, y);
        System.out.println(r);
    }

    public static String int_multi(String x, String y){
        if(x.length()==1){
            return String.valueOf(Integer.parseInt(x)*Integer.parseInt(y));
        }
        String a = x.substring(0,x.length()/2);
        String b = x.substring(x.length()/2,x.length());
        String c = y.substring(0,y.length()/2);
        String d = y.substring(y.length()/2,y.length());

        String ac = int_multi(a,c);
        String bd = int_multi(b,d);

        int a_ = Integer.parseInt(a);
        int b_ = Integer.parseInt(b);
        int c_ = Integer.parseInt(c);
        int d_ = Integer.parseInt(d);

        long ac_ = Long.parseLong(ac);
        long bd_ = Long.parseLong(bd);
        long _ad_bc = (a_ + b_)*(c_ + d_) - ac_ - bd_;

        long result = ac_ * Math.round(Math.pow(10,x.length()))+_ad_bc*Math.round(Math.pow(10,x.length()/2))+bd_;
        return String.valueOf(result);
    }
}