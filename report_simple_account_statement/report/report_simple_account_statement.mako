<html>
<head>
<style type="text/css">
	${css} 
</style>
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

<div>
			<table>
					<tr>
						<td width='14.28%' align='center'>
							${_('Document Date') | entity}	
						</td>
						<td width='14.28%' align='center'>
							${_('Document') | entity}
						</td>
						<td width='14.28%' align='center'>
							${_('Due Date') | entity}
						</td>
						<td width='14.28%' align='center'>
							${_('Journal') | entity}
						</td>
						<td width='14.28%' align='center'>
							${_('Currency') | entity}
						</td> 
						<td width='14.28%' align='center'>
							${_('Credit') | entity}
						</td>
						<td width='14.28%' align='center'>
							${_('Debit') | entity}
						</td>
						<td width='14.28%' align='center'>
							${_('Current Balance') | entity}
						</td>
					</tr>
<% current_period=get_current_period(data)%>
% for o in 	get_invoices(data):
					<tr>
    					<td colspan="8" align="right">
    					${_(' Last Balance') | entity} : ${formatLang(get_accumulate_balance(o.partner_id.id,current_period),monetary=True)}
    				 	</td>
    				</tr>
		%if (o.period_id.id == current_period):
					<tr>
						<td width='14.28%' align='center'>
							${formatLang(o.date_invoice,date=True) }
						</td>
						<td width='14.28%' align='center'>
							${o.number}
						</td>
						<td width='14.28%' align='center'>
							${formatLang(o.date_due,date=True) }
						</td>
						<td  width='14.28%' align='center'>
							${o.journal_id.code}
						</td>
						<td width='14.28%' align='center'>
							${o.currency_id.name}
						</td>
						<td width='14.28%' align='center'>
							${'-'}${formatLang(o.amount_total,monetary=True)}
						</td>
						<td width='14.28%' align='center'>
									  	
						</td>
					</tr>
		%endif
		<% residual= get_accumulate_balance(o.partner_id.id,current_period) %>
		%for payment in range(0,len(o.payment_ids)): 
			%if (o.payment_ids[int(payment)].period_id.id == current_period):
				<%  
				if(residual > 0):
					residual = residual - o.payment_ids[int(payment)].debit
				else:
					residual = o.amount_total - o.payment_ids[int(payment)].debit
				%>
					 <tr>
						<td width='14.28%' align='center'>
						
							${formatLang(o.payment_ids[int(payment)].date_created,date=True)}
						</td>
						<td width='14.28%' align='center'>
						    ${o.payment_ids[int(payment)].move_id.name}
						</td>
						</td>
						<td width='14.28%' align='center'>
							##${payments_obj}
						</td>
						<td  width='14.28%' align='center'>
							${o.payment_ids[int(payment)].journal_id.code}
						</td>	
						<td width='14.28%' align='center'>
							
						</td>
						<td width='14.28%' align='center'>
							
						</td>
						<td width='14.28%' align='center'>
							${'+'}${formatLang(o.payment_ids[int(payment)].debit,monetary=True)}
						</td>
						</td>
						<td width='14.28%' align='center'>
							 ${formatLang(residual,monetary=True)} 
						</td>
					</tr>
    				<br>
    		%endif
    	%endfor
    				<td  colspan="2" align="left">
					${_('Document Total')}${': '}${formatLang(o.amount_total,monetary=True) | entity}
					</td>
					<td  colspan="3" align="left">
					${_('Payments')}${': '}${formatLang(get_total_payments(o.payment_ids,current_period),monetary=True) or '0.00' |entity}
					</td>
					<td  colspan="3" align="right">
					${_('Balance')}${': '}${formatLang(abs(get_accumulate_balance(o.partner_id.id,current_period)-get_total_payments(o.payment_ids,current_period)),monetary=True) |entity}
					</td>
			</table>
%endfor			
</div>
<p style="page-break-before: always;"></p>
</body>
</html>