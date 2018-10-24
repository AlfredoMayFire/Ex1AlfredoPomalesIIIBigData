import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;

public class KeywordToTweetsReducer extends Reducer<Text, Text, Text, Text> {
    @Override
    protected void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException{

        StringBuilder myList = new StringBuilder();

        for (Text value : values)
            myList.append( ", " + value );

        context.write(key, new Text(myList.toString()));

    }
}
