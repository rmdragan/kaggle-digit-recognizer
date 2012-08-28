from random import sample

def random_undersample(dataset, sample_size=-1, sample_percent=-1):
    """Randomply undersamples without replacemnt a dataset."""
    # determine sample size
    try:
        if 0 <= sample_size <= len(dataset):
            s_size = int(sample_size)
        elif 0 <= sample_percent <= 100:
            s_size = int(len(dataset) * sample_percent / 100)
        else:
            s_size = 0
    except:
        return []
    # return sample
    return sample(dataset, s_size)

if __name__ == '__main__':
    from IO import read_csv, write_csv, read_header
    file_path = '../data/train.csv'
    out_file_path = '../data_preprocessed/train_undersampled.csv'
    # read dataset
    dataset = read_csv(file_path, has_header=True)
    header = read_header(file_path)
    # undersample
    sample = random_undersample(dataset, sample_percent=5)
    # write to file
    write_csv(out_file_path , sample, header=header)
