<html>
<head>
<style type="text/css">
	${css} 
</style>
</head>
<body>
<div class="container">
	<div>
		<div>
			% for o in 	get_company_info(data):
				<div>${helper.embed_image('jpeg',str(o.logo_web),250, 120)}</div>
			% endfor
			<h3 class="title">
				${_('ACCOUNT SIMPLE STATEMENT REPORT')}
			</h3>
		</div>
	</div>
	<div>
		<div >
			<table>
				<thead>
					<tr>
						<th>
							${_('INVOICE DATE')}	
						</th>
						<th>
							${_('INVOICE NUMBER')}
						</th>
						<th>
							${_('JOURNAL')}
						</th>
						<th>
							${_('CURRENCY')}
						</th>
						<th>
							${_('CREDIT')}
						</th>
						<th>
							${_('DEBIT')}
						</th>
				</thead>
				<tbody>
				% for o in 	get_result(data):
					<tr class="active">
						<td>
							${o.date_invoice}
							<br>
						</td>
						<td  >
							${o.number}
							<br>
						</td>
						<td  >
							${o.journal_id.code}
							<br>
						</td>
						<td  >
							${o.currency_id.name}
							##${formatLang(get_total_debit_credit(o.line_id)['sum_tot_debit']) or '0.00' |entity}
							<br>
						</td>
						<td  >
							${o.amount_total}
							<br>
						</td>
						<td  >
							${o.amount_total}
							<br>
						</td>
					</tr>
					
				</tbody>
			</table>
			
		</div>
	</div>
	<div>
		<div>
		</div>
	</div>
</div>
% endfor
</body>
</html>