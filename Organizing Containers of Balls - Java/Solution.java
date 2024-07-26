import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


class Result {

      public static int countBalls(List<Integer> container){
        int ballCount = 0;
        for(Integer ballCountType : container){
                ballCount += ballCountType;
        }
        return ballCount;
    }

    public static String organizingContainers(List<List<Integer>> containers) {
        List<Integer> containerSizes = new ArrayList<>();
        int[] typeCounts = new int[containers.size()];
        for(List<Integer> container : containers){
            containerSizes.add(countBalls(container));
            for(int i = 0; i < container.size(); i++){
                    typeCounts[i] += container.get(i);
            }
        }

        for(int i = 0;i < typeCounts.length;i++){
            int index = containerSizes.indexOf(typeCounts[i]);
            if(index == -1){
                return "Impossible";
            }
            else {
                containerSizes.remove(index);
            }
        }
        return "Possible";
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        IntStream.range(0, q).forEach(qItr -> {
            try {
                int n = Integer.parseInt(bufferedReader.readLine().trim());

                List<List<Integer>> container = new ArrayList<>();

                IntStream.range(0, n).forEach(i -> {
                    try {
                        container.add(
                            Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                                .map(Integer::parseInt)
                                .collect(toList())
                        );
                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }
                });

                String result = Result.organizingContainers(container);

                bufferedWriter.write(result);
                bufferedWriter.newLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        bufferedReader.close();
        bufferedWriter.close();
    }
}
