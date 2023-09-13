import click
import requests
from tabulate import tabulate
from datetime import timezone
import datetime

@click.command()

@click.option('--count', default=10, help='Number of Contests')

def cli(count):
	"""
	A basic command line tool to show the upcoming competitive programming contests
	"""
	now = datetime.datetime.now()
	format_iso_now = now.isoformat()
	url = "https://clist.by:443/api/v1/contest/?limit="+ str(count) + "&start__gt="+format_iso_now+"&order_by=start"
	headers = {
	'Authorization' : "ApiKey aditya97:7343ff4fce6cc3997a2367f50ff0af3b642ce173"
	}
	r = requests.get(url=url,headers=headers)
	contest_list = r.json()['objects']
	table_list = list()
	for contest in contest_list:
		table_row = list()
		table_row.append(contest['event'])
		table_row.append(contest['resource']['name'])
		start_time = datetime.datetime.strptime(contest['start'],"%Y-%m-%dT%H:%M:%S")
		start_time = str(start_time)
		end_time = datetime.datetime.strptime(contest['end'],"%Y-%m-%dT%H:%M:%S")
		end_time = str(end_time)
		table_row.append(start_time + " UTC")
		table_row.append(end_time + " UTC")
		# Append To Table
		table_list.append(table_row)
	print(tabulate(table_list,headers=['Contest Name','Host','Start','End']))

if __name__ == "__main__":
	cli()