import java.util.HashSet;
import java.util.Set;

public class duplicate {
    static boolean duplicates(final int[] zipcodelist) {
        Set<Integer> lump = new HashSet<Integer>();
        for (int i : zipcodelist) {
            if (lump.contains(i))
                return true;
            lump.add(i);
        }
        return false;
    }

    public static void main(String[] args) {
        int [] arr = {20,10,5};
        System.out.println(duplicates(arr));
    }
}
