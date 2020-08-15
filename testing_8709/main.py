import sys
import click

@click.command()
@click.option('--count',default=1,help='Number of prints required')
@click.option('--name',help='name to print')
def hello(count,name):
    '''Click Cli testing'''
    for x in range(count):
        click.echo('Hello %s' %name)

if __name__ == '__main__':
    hello()