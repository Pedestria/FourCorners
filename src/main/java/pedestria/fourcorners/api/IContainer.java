package pedestria.fourcorners.api;

import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.entity.player.InventoryPlayer;
import net.minecraft.item.ItemStack;

public interface IContainer

/*
 * This INTERFACE is ONLY used on the main classes of containers that involve
 * interacting with the main inventory
 */
{
	public void initPlayerInventory(InventoryPlayer inventoryPlayer);
	
	//@Override
	public ItemStack transferStackInSlot(EntityPlayer player, int index);
}
