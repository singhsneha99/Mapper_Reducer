# MapReduce Word Count

This project demonstrates a basic Word Count implementation using MapReduce in Python.

## Files

- `pmapper.py` - The mapper code that processes the input data. It splits each line into words and outputs a key/value pair of word and count of 1.

- `preducer.py` - The reducer code that aggregates the data by word. It sums up the count values for each word and outputs the word with the total count.

## Usage

To run the MapReduce job:

1. Input data: Place some text files in the `input/` folder. 

2. Run the mapper: `cat input/* | python mapper.py > output.txt`

This will run the mapper on each input file and direct the output to output.txt

3. Run the reducer: `python reducer.py < output.txt` 

This will process the mapper output and print the final word counts to stdout.

The code can be easily adapted to run distributed across a Hadoop cluster by configuring the input and output directories.

## Explanation

The mapper reads each line, splits it into words and outputs a key/value pair of:

```
word \t 1
```

The reducer aggregates all values for each word by keeping a running sum. It outputs:

```
word \t total_count  
```

This gives the final count for each word across all input files.
