import java.util.Arrays;

/**
 * test
 */
public class longestCommmonPrefix_5 {

    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";

        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length - 1];
        int c = 0;
        while (c < first.length()) {
            if (first.charAt(c) == last.charAt(c))
                c++;
            else
                break;
        }
        return c == 0 ? "" : first.substring(0, c);
    }

    public static void main(String[] args) {

        String strs[] = {"opposite","almight","all","optimistic","ops"};

        longestCommmonPrefix_5 obj = new longestCommmonPrefix_5();

       System.out.println(obj.longestCommonPrefix(strs));

    }
}