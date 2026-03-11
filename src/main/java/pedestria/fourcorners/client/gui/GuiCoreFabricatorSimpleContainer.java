package pedestria.fourcorners.client.gui;

import java.awt.Color;

import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.inventory.GuiContainer;
import net.minecraft.entity.player.InventoryPlayer;
import net.minecraft.util.ResourceLocation;
import net.minecraft.util.text.TextComponentTranslation;
import pedestria.fourcorners.container.ContainerCoreFabricatorSimple;
import pedestria.fourcorners.tiles.TileEntityCoreFabricatorSimple;
import pedestria.fourcorners.util.Reference;

public class GuiCoreFabricatorSimpleContainer extends GuiContainer {
	
	private static final ResourceLocation texture = new ResourceLocation(Reference.MODID, "textures/gui/core_fabricator.png");

	public GuiCoreFabricatorSimpleContainer(InventoryPlayer player, TileEntityCoreFabricatorSimple coreFabricatorSimple) 
	{
		super(new ContainerCoreFabricatorSimple(player, coreFabricatorSimple));
		xSize = 176;
		ySize = 166;
	}

	@Override
	protected void drawGuiContainerBackgroundLayer(float partialTicks, int mouseX, int mouseY) {
		Minecraft.getMinecraft().getTextureManager().bindTexture(texture);
		drawTexturedModalRect(guiLeft, guiTop,0,0,xSize,ySize);
	}
	
	@Override
	protected void drawGuiContainerForegroundLayer(int mouseX, int mouseY) {
	
		fontRenderer.drawString(new TextComponentTranslation ("tile.container_core_fabricator_simple.name").getFormattedText(), 5,5,Color.darkGray.getRGB());
		
	}

}
