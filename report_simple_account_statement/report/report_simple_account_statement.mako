<html>
<head>
<style type="text/css">
	${css} 
</style>
<style type="text/css">.table_line{
    vertical-align:middle;
    
    background-color:#ffffff;

    border:1px solid #ffffff;
    border-width:0px 1px 1px 0px;
    text-align:center;
    padding:7px;
    font-size:10px;
    font-family:Arial;
    font-weight:normal;
    color:#000000;
}</style>
</head>
<body>
<% setLang(user.lang) %>
<div>
		<div>
			% for o in 	get_company_info(data):
				<div>${helper.embed_image('jpeg',str(o.logo_web),250, 120)}</div>
			% endfor
			<h3 class="title">
				${_('ACCOUNT SIMPLE STATEMENT REPORT') | entity}
			</h3>
		</div>
</div>

<div class="table_standard">
			<table>
					<tr>
						<td>
							${_('INVOICE DATE') | entity}	
						</td>
						<td>
							${_('INVOICE NUMBER') | entity}
						</td>
						<td>
							${_('JOURNAL') | entity}
						</td>
						<td>
							${_('CURRENCY') | entity}
						</td>
						<td>
							${_('CREDIT') | entity}
						</td>
						<td>
							${_('DEBIT') | entity}
						</td>
					</tr>
% for o in 	get_result(data):
					<tr>
						<td   width='20%' class="table_line">
							${formatLang(o.date_invoice,date=True) }
						</td>
						<td>
							${o.number}
						</td>
						<td  width='20%'>
							${o.journal_id.code}
						</td>
						<td  width='20%'>
							${o.currency_id.name}
							##${formatLang(get_total_debit_credit(o.line_id)['sum_tot_debit']) or '0.00' |entity}
						</td>
						<td  width='20%'>
							${ formatLang(o.amount_total) or '0.00' }
						</td>
						<td  width='20%'>
						<br>	
						%for payment in range(0 ,len(o.payment_ids)): 
									
									${formatLang(o.payment_ids[int(payment)].debit) or '0.0'}
						%endfor						  	
						</td>
					</tr>
					 </br>
    				
			</table>
</div>
% endfor
<p style="page-break-before: always;"></p>
</body>
</html>