import torch

def main():
    # YOUR CODE HERE
    print('Hello')

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description="Torch Hub Testing")
    parser.add_argument('--repository', type=str, required=True, help='Repository, username/reponame')
    parser.add_argument('--tag', type=str, required=True, help='Release tag')
    args = parser.parse_args()

    weights = torch.hub.list(f'{args.repository}:{args.tag}', force_reload=True)

    for weight in weights:
        model = torch.hub.load(f'{args.repository}:{args.tag}', weight)
        print(f'[INFO] Success load {weight.upper()}')